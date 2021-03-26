window.cookieconsent.initialise({
    container: document.getElementById("content"),
    palette: {
        popup: {
            background: "#fff"
        },
        button: {
            background: "#aa6ab2",
            text: "#fff"
        }
    },
    theme: "classic",
    type: "opt-out",
    content: {
        message: "Het agentschap Onroerend Erfgoed gebruikt cookies om de goede werking van onze website te verzekeren en jouw surfervaring te verbeteren. Meer informatie over de cookies die we gebruiken lees je in <a href=https://www.onroerenderfgoed.be/cookiebeleid>ons cookiebeleid</a>. Voor het gebruik van sociale media cookies hebben wij jouw toestemming nodig. Deze cookies gebruiken we om sociale media, zoals Facebook, Twitter of YouTube, te linken aan onze website. Zo kan je bijvoorbeeld artikels delen op sociale media of bepaalde inhoud van die sites op deze website bekijken. Wil je hiervan kunnen genieten?",
        deny: "<a href=https://www.onroerenderfgoed.be/#>Nee, ga verder naar de website</a>",
        allow: "Ja, ik geef toestemming"
    },
    revokable: true,
    onStatusChange: function (status) {
        console.log(this.hasConsented() ?
            'enable cookies' : 'disable cookies');
    },
    law: {
        regionalLaw: false,
    },
    location: true,
    showLink: false
});