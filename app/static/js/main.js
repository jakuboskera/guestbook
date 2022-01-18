document.getElementById('anonymous').onchange = function() {
    document.getElementById('name').disabled = this.checked;
};

new FgEmojiPicker({
    trigger: ['#emoji'],
    position: ['bottom', 'right'],
    dir: "/static/js/",
    emit(obj, triggerElement) {
        const emoji = obj.emoji;
        document.querySelector('textarea').value += emoji;
    }
});
