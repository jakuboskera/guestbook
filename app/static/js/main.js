if (document.getElementById('anonymous')) {
    document.getElementById('anonymous').onchange = function() {
        var name = document.getElementById('name');
        name.disabled = this.checked;
        name.value = "";
    }
}

(function() {
    var onpageLoad = localStorage.getItem("theme") || "";
    var body = document.body.classList;

    if (onpageLoad == "bootstrap-dark") {
        body.remove("bootstrap");
        body.add("bootstrap-dark")
        document.getElementById('toggle-dark-mode').checked = true;
    }
})();


function SwapThemes() {
    console.log("hi");
    var body = document.body.classList;

    if (body.contains("bootstrap")) {
        body.remove("bootstrap");
        body.add("bootstrap-dark");
    } else {
        body.remove("bootstrap-dark");
        body.add("bootstrap");
    }

    var theme = localStorage.getItem("theme");
    if (theme && theme === "bootstrap-dark") {
        localStorage.setItem("theme", "");
    } else {
        localStorage.setItem("theme", "bootstrap-dark");
    }
}

new FgEmojiPicker({
    trigger: ['#emoji'],
    position: ['bottom', 'right'],
    dir: "/static/js/",
    emit(obj, triggerElement) {
        const emoji = obj.emoji;
        document.querySelector('textarea').value += emoji;
    }
});
