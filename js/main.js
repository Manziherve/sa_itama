// JS de base pour interactions (menu, slider, etc.)
document.addEventListener('DOMContentLoaded', function() {
  // Menu mobile toggle
  const menuBtn = document.getElementById('menu-btn');
  const nav = document.getElementById('nav');
  if(menuBtn && nav) {
    menuBtn.addEventListener('click', () => {
      nav.classList.toggle('hidden');
    });
  }
  // Ajoute ici d'autres interactions JS si besoin
});
