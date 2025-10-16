const savedTheme = localStorage.getItem('theme');

if (savedTheme) {
    document.body.classList.toggle('light-mode', savedTheme === "light");
} else {
    const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
    document.body.classList.toggle('light-mode', prefersLight)
}