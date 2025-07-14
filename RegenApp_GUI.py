import customtkinter
from RegenFinder import trouver_joueur_original, FICHIER_CSV 

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Regen Finder FC25")
        self.geometry("700x650")

        
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.pack(padx=20, pady=20, fill="x")

        self.natio_label = customtkinter.CTkLabel(self.input_frame, text="Nationalité :")
        self.natio_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.natio_entry = customtkinter.CTkEntry(self.input_frame, placeholder_text="France")
        self.natio_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.poste_label = customtkinter.CTkLabel(self.input_frame, text="Poste(s) :")
        self.poste_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.poste_entry = customtkinter.CTkEntry(self.input_frame, placeholder_text="ST, CF")
        self.poste_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        self.jour_label = customtkinter.CTkLabel(self.input_frame, text="Jour naissance :")
        self.jour_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.jour_entry = customtkinter.CTkEntry(self.input_frame, placeholder_text="19")
        self.jour_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.mois_label = customtkinter.CTkLabel(self.input_frame, text="Mois naissance :")
        self.mois_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.mois_entry = customtkinter.CTkEntry(self.input_frame, placeholder_text="12")
        self.mois_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        
        self.input_frame.grid_columnconfigure(1, weight=1)

        self.search_button = customtkinter.CTkButton(self, text="Trouver le Joueur Original", command=self.search_player)
        self.search_button.pack(padx=20, pady=10, fill="x")

        self.results_textbox = customtkinter.CTkTextbox(self, height=250)
        self.results_textbox.pack(padx=20, pady=20, fill="both", expand=True)
        self.results_textbox.configure(state="disabled") 

    def search_player(self):
        """Cette fonction est appelée quand on clique sur le bouton."""
        nationalite = self.natio_entry.get()
        poste = self.poste_entry.get()
        jour = int(self.jour_entry.get()) if self.jour_entry.get().isdigit() else None
        mois = int(self.mois_entry.get()) if self.mois_entry.get().isdigit() else None
        resultat = trouver_joueur_original(nationalite, poste, jour, mois, FICHIER_CSV)
        self.results_textbox.configure(state="normal") 
        self.results_textbox.delete("1.0", "end") 
        
        if resultat:
            self.results_textbox.insert("end", f"✅ {len(resultat)} joueur(s) trouvé(s) :\n\n")
            resultat.sort(key=lambda x: int(x['overall']), reverse=True)
            for joueur in resultat:
                fiche = (
                    f"- {joueur.get('first_name', '')} {joueur.get('last_name', '')} (Âge: {joueur.get('age', 'N/A')})\n"
                    f"  Date de naissance: {joueur.get('birthdate', 'N/A')}\n"
                    f"  Note: {joueur['overall']} | Potentiel: {joueur['potential']}\n"
                    f"  Club: {joueur['owner_team']} | Poste(s): {joueur['preferred_position']}\n\n"
                )
                self.results_textbox.insert("end", fiche)
        else:
            self.results_textbox.insert("end", "❌ Aucun joueur original trouvé pour ce profil.")

        self.results_textbox.configure(state="disabled") 

if __name__ == "__main__":
    app = App()
    app.mainloop()