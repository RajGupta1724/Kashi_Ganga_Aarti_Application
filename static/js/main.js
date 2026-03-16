/* ================================================
   Kashi Ganga — Main JavaScript
   ================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ===== NAVBAR SCROLL EFFECT ===== */
  const nav = document.getElementById('mainNav');
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 60) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ===== BACK TO TOP BUTTON ===== */
  const backToTop = document.getElementById('backToTop');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ===== SCROLL REVEAL ANIMATION ===== */
  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Stagger delay for sibling elements
        const siblings = entry.target.parentElement
          ? Array.from(entry.target.parentElement.querySelectorAll('.fade-in-up:not(.visible)'))
          : [];
        const delay = Math.min(siblings.indexOf(entry.target) * 80, 320);
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, delay);
        revealObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-in-up').forEach(el => revealObserver.observe(el));

  /* ===== STATS COUNTER ANIMATION ===== */
  const counterElements = document.querySelectorAll('.hero-stat-number, .stat-number');
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counterElements.forEach(el => counterObserver.observe(el));

  function animateCounter(el) {
    const text = el.textContent.trim();
    const match = text.match(/^(\d+)/);
    if (!match) return;

    const target = parseInt(match[1]);
    const suffix = text.replace(match[1], '');
    const duration = 1500;
    const start = performance.now();

    function update(time) {
      const elapsed = time - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      const current = Math.round(eased * target);
      el.textContent = current + suffix;
      if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  /* ===== GALLERY FILTER (for gallery page) ===== */
  const filterBtns = document.querySelectorAll('.gallery-filter-btn[data-filter]');
  const galleryItems = document.querySelectorAll('.gallery-page-item[data-category]');

  if (filterBtns.length && galleryItems.length) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const filter = this.dataset.filter;

        filterBtns.forEach(b => b.classList.remove('active'));
        this.classList.add('active');

        galleryItems.forEach(item => {
          if (filter === 'all' || item.dataset.category === filter) {
            item.style.display = '';
            item.style.opacity = '0';
            item.style.transform = 'scale(0.9)';
            requestAnimationFrame(() => {
              item.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
              item.style.opacity = '1';
              item.style.transform = 'scale(1)';
            });
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  /* ===== BOOKING FORM ENHANCEMENTS ===== */
  const bookingForm = document.getElementById('bookingForm');
  if (bookingForm) {
    const inputs = bookingForm.querySelectorAll('.form-control, .form-select');

    inputs.forEach(input => {
      // Add success state on valid blur
      input.addEventListener('blur', function () {
        if (this.value.trim()) {
          this.style.borderColor = '#28a745';
        } else {
          this.style.borderColor = '';
        }
      });

      input.addEventListener('focus', function () {
        this.style.borderColor = 'var(--primary)';
      });
    });

    // Prevent past dates in event_date
    const dateInput = bookingForm.querySelector('input[type="date"]');
    if (dateInput) {
      const today = new Date().toISOString().split('T')[0];
      dateInput.min = today;
    }

    // Loading state on submit
    bookingForm.addEventListener('submit', function () {
      const btn = this.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Submitting...';
      }
    });
  }

  /* ===== WHATSAPP PULSE ===== */
  const fab = document.querySelector('.whatsapp-fab');
  if (fab) {
    let pingCount = 0;
    const pingInterval = setInterval(() => {
      if (pingCount >= 3) {
        clearInterval(pingInterval);
        return;
      }
      fab.style.transform = 'scale(1.15)';
      setTimeout(() => { fab.style.transform = ''; }, 300);
      pingCount++;
    }, 4000);
  }

  /* ===== ACTIVE NAV LINK ===== */
  const currentPath = window.location.pathname;
  document.querySelectorAll('#mainNav .nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  /* ===== SMOOTH SCROLL FOR ANCHOR LINKS ===== */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ===== AUTO-DISMISS MESSAGES ===== */
  const alerts = document.querySelectorAll('.alert.alert-dismissible');
  alerts.forEach(alert => {
    setTimeout(() => {
      if (alert) {
        alert.style.transition = 'opacity 0.5s ease';
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 500);
      }
    }, 5000);
  });

  /* ===== NAVBAR MOBILE CLOSE ON CLICK ===== */
  const navLinks = document.querySelectorAll('#navMenu .nav-link');
  const navCollapse = document.getElementById('navMenu');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navCollapse && navCollapse.classList.contains('show')) {
        const collapseInstance = bootstrap.Collapse.getOrCreateInstance(navCollapse);
        collapseInstance.hide();
      }
    });
  });

});

/* ===== LIGHTBOX (available globally) ===== */
window.openLightbox = function (src, caption) {
  const lb = document.getElementById('lightbox');
  if (!lb) return;
  document.getElementById('lightboxImg').src = src;
  const cap = document.getElementById('lightboxCaption');
  if (cap) cap.textContent = caption || '';
  lb.classList.add('active');
  document.body.style.overflow = 'hidden';
};

window.closeLightbox = function (e) {
  const lb = document.getElementById('lightbox');
  if (!lb) return;
  if (!e || e.target === lb || (e.target && e.target.closest && e.target.closest('.lightbox-close'))) {
    lb.classList.remove('active');
    document.getElementById('lightboxImg').src = '';
    document.body.style.overflow = '';
  }
};

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') window.closeLightbox();
});
