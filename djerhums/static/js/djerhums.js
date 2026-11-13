document.addEventListener("DOMContentLoaded", function () {
    var motif = document.getElementById("id_motif");
    var blocs = document.querySelectorAll(".champ-produits_commandes, .champ-quantite");

    if (!motif || blocs.length === 0) {
        return;
    }

    function afficherBlocCommande() {
        var estCommande = motif.value === "Commande";
        blocs.forEach(function (bloc) {
            bloc.hidden = !estCommande;
        });
    }

    motif.addEventListener("change", afficherBlocCommande);
    afficherBlocCommande();
});