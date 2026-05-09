import mysql.connector
from datetime import date


# -------- BANCO --------
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='projeto_cdc',
    )


def create_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_tarefas (
            id_tarefa INT AUTO_INCREMENT PRIMARY KEY,
            nome_tarefa VARCHAR(100),
            descricao TEXT,
            prioridade VARCHAR(10),
            status VARCHAR(15),
            data_criacao DATE
        )
    """)

    conexao.commit()
    cursor.close()
    conexao.close()


# -------- VALIDAÇÃO --------
def validar_prioridade(p):
    return p in ["Baixa", "Média", "Alta"]


# -------- FUNÇÕES CRIAR --------
def criar():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tbl_tarefas
        (nome_tarefa, descricao, prioridade, status, data_criacao)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        entry_nome.get(),
        entry_desc.get(),
        combo_prioridade.get(),
        combo_status.get(),
        date.today()
    ))

    conexao.commit()
    cursor.close()
    conexao.close()

    listar()
    limpar()

    from tkinter import messagebox
    messagebox.showinfo("Sucesso", "Tarefa criada!")

# -------- FUNÇÕES LISTAR --------

def listar():
    textbox.delete("0.0", "end")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tbl_tarefas")

    for row in cursor.fetchall():
        texto = f"""
ID: {row[0]}
Nome: {row[1]}
Descrição: {row[2]}
Prioridade: {row[3]}
Status: {row[4]}
Data: {row[5]}
----------------------------
"""
        textbox.insert("end", texto)

    cursor.close()
    conexao.close()

# -------- FUNÇÕES DELETAR --------

def deletar():
    id_tarefa = entry_id.get()

    if not id_tarefa:
        from tkinter import messagebox
        messagebox.showwarning("Erro", "Digite o ID")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM tbl_tarefas WHERE id_tarefa=%s",
        (id_tarefa,)
    )

    conexao.commit()
    cursor.close()
    conexao.close()

    listar()
    limpar()

# -------- FUNÇÕES UPDATE --------

def atualizar():
    id_tarefa = entry_id.get()

    if not id_tarefa:
        from tkinter import messagebox
        messagebox.showwarning("Erro", "Digite o ID")
        return

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tbl_tarefas
        SET nome_tarefa=%s,
            descricao=%s,
            prioridade=%s,
            status=%s
        WHERE id_tarefa=%s
    """, (
        entry_nome.get(),
        entry_desc.get(),
        combo_prioridade.get(),
        combo_status.get(),
        id_tarefa
    ))

    conexao.commit()
    cursor.close()
    conexao.close()

    listar()
    limpar()


def limpar():
    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_desc.delete(0, "end")
    combo_prioridade.set("")
    combo_status.set("Pendente")


# ---------------------------------------------------------
# INTERFACE APENAS AO EXECUTAR app.py
# ---------------------------------------------------------

if __name__ == "__main__":

    import customtkinter as ctk
    from tkinter import messagebox

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    create_tabela()

    app = ctk.CTk()
    app.title("Gerenciador de Tarefas - CDC.3NA")
    app.geometry("1000x600")


    # SIDEBAR
    sidebar = ctk.CTkFrame(app, width=200)
    sidebar.pack(side="left", fill="y")

    ctk.CTkLabel(
        sidebar,
        text="MENU",
        font=("Arial", 18)
    ).pack(pady=20)

    ctk.CTkButton(
        sidebar,
        text="Listar Tarefas",
        command=listar
    ).pack(pady=10)

    ctk.CTkButton(
        sidebar,
        text="Limpar Campos",
        command=limpar
    ).pack(pady=10)


    # MAIN
    main = ctk.CTkFrame(app)
    main.pack(fill="both", expand=True, padx=10, pady=10)

    ctk.CTkLabel(
        main,
        text="Gerenciador de Tarefas",
        font=("Arial", 20, "bold")
    ).pack(pady=10)


    # CAMPOS
    entry_id = ctk.CTkEntry(
        main,
        placeholder_text="ID (para atualizar/deletar)"
    )
    entry_id.pack(pady=5)

    entry_nome = ctk.CTkEntry(
        main,
        placeholder_text="Nome da tarefa"
    )
    entry_nome.pack(pady=5)

    entry_desc = ctk.CTkEntry(
        main,
        placeholder_text="Descrição"
    )
    entry_desc.pack(pady=5)

    combo_prioridade = ctk.CTkComboBox(
        main,
        values=["Baixa", "Média", "Alta"]
    )
    combo_prioridade.pack(pady=5)

    combo_status = ctk.CTkComboBox(
        main,
        values=["Pendente", "Concluída"]
    )
    combo_status.pack(pady=5)

    combo_status.set("Pendente")


    # BOTÕES
    btn_frame = ctk.CTkFrame(main)
    btn_frame.pack(pady=10)

    ctk.CTkButton(
        btn_frame,
        text="Criar",
        command=criar
    ).grid(row=0, column=0, padx=10)

    ctk.CTkButton(
        btn_frame,
        text="Atualizar",
        command=atualizar
    ).grid(row=0, column=1, padx=10)

    ctk.CTkButton(
        btn_frame,
        text="Deletar",
        command=deletar
    ).grid(row=0, column=2, padx=10)


    # ÁREA DE TEXTO
    textbox = ctk.CTkTextbox(
        main,
        width=600,
        height=250
    )
    textbox.pack(pady=10)


    listar()

    app.mainloop()
