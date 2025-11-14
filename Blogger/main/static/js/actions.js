document.addEventListener('DOMContentLoaded', () => {

  // Language Switch
  const langBtn = document.getElementById('lang-toggle');

  if (langBtn) {
    langBtn.addEventListener('click', (e) => {
      e.preventDefault();

      const cookies = document.cookie.split(';').reduce((acc, c) => {
        const [key, value] = c.trim().split('=');
        acc[key] = value;
        return acc;
      }, {});
      const currentLang = cookies['django_language'] || 'ar';
      const nextLang = currentLang === 'en' ? 'ar' : 'en';


      setTimeout(() => {
        window.location.href = `/set-language/${nextLang}/?HTTP_REFERER=${encodeURIComponent(window.location.href)}`;
      }, 150);
    });
  }

  // Theme Switch
  const themeBtn = document.getElementById('theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const icon = themeBtn.querySelector('.material-icons');
      const mode = icon.textContent.trim() === 'dark_mode' ? 'light' : 'dark';
      window.location.href = `/set-theme/${mode}/?HTTP_REFERER=${encodeURIComponent(window.location.href)}`;
    });
  }

  // Mobile Menu
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');

  toggleBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });

});