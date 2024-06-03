
document.getElementById('filtro').addEventListener('change', function () {
    let url = new URL(window.location.href);
    if (this.checked) {
        url.searchParams.set('filtro', 'on');
    } else {
        url.searchParams.delete('filtro');
    }
    window.location.href = url.toString();
});
