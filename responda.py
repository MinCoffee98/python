import tkinter as tk
from tkinter import messagebox

# Gerar 50 perguntas pessoais fictícias
def generate_questions():
    questions = [
        "Qual é o seu livro favorito?",
        "Qual é o seu filme favorito?",
        "Qual é a sua música favorita?",
        "Qual é a sua comida favorita?",
        "Qual é o seu esporte favorito?",
        "Qual é a sua cor favorita?",
        "Qual é o seu hobby preferido?",
        "Qual é o seu animal favorito?",
        "Qual é o seu lugar favorito para viajar?",
        "Qual é a sua estação do ano favorita?",
        "Qual é a música que te dá mais vontade de dançar?",
        "Qual é o próximo sonho que você quer realizar na sua vida?",
        "Qual é a comida que você experimentou, mas nunca mais comeria?",
        "Como você gosta de passar seus aniversários?",
        "Que tipo de presente você gosta?",
        "Qual é a última coisa que você faz antes de dormir?",
        "Você já teve algum apelido constrangedor?",
        "Você quer ter filhos? Por quê? Quantos?",
        "Você sonha em se casar algum dia?",
        "Qual idioma você quer aprender algum dia?",
        "Tem medo de algum inseto?",
        "O que te faz rir?",
        "Qual é a primeira coisa que você gostaria que mais pessoas soubessem sobre você?",
        "Três coisas que você quer fazer antes de morrer?",
        "Qual cheiro que você ama sentir?",
        "Você fala sozinho?",
        "O que gostaria de fazer no seu aniversário?"
      ]
  
    while len(questions) < 27:
        questions.extend(questions[:27 - len(questions)])
    return questions

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Perguntas")
        self.root.geometry("600x400")
        self.root.configure(background='black')

        self.questions = generate_questions()
        self.current_question = 0
        self.responses = []

        self.question_label = tk.Label(root, text="", bg='black', fg='white', font=('Arial', 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, bg='white', fg='black', font=('Arial', 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Enviar Resposta", bg='white', fg='black', font=('Arial', 14), command=self.submit_answer)
        self.submit_button.pack(pady=20)

        self.next_button = tk.Button(root, text="Próxima", bg='white', fg='black', font=('Arial', 14), command=self.next_question)
        self.next_button.pack(pady=20)
        self.next_button.config(state=tk.DISABLED)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        answer = self.answer_entry.get()
        if answer:
            self.responses.append(answer)
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Atenção", "Por favor, escreva uma resposta antes de avançar.")

    def next_question(self):
        self.current_question += 1
        if self.current_question >= len(self.questions):
            self.show_results()
        else:
            self.show_question()

    def show_results(self):
        results_text = "Aqui estão suas respostas:\n\n"
        for i, response in enumerate(self.responses):
            results_text += f"{self.questions[i]}: {response}\n"
        messagebox.showinfo("Suas Respostas", results_text)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()
