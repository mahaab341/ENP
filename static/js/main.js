(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    }); 
    //Packages carousel
  $(document).ready(function(){
      $(".testimonial-carousel").owlCarousel({
          autoplay:true,
          smartSpeed:500,
          margin:25,
          dots:true,
          loop:true,
          nav:true,
          responsive:{
              0:{items:1},
              768:{items:2},
              992:{items:3}
          }
      });
  });



    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);
  const sections = document.querySelectorAll('.asection');
    const indicators = document.querySelectorAll('.indicator');
    let current = 0;
    let autoSlide;

    function showSection(index) {
      sections.forEach((s, i) => s.classList.toggle('active', i === index));
      indicators.forEach((dot, i) => dot.classList.toggle('active', i === index));
      current = index;
    }

    function nextSlide() {
      let next = current + 1 < sections.length ? current + 1 : 0;
      showSection(next);
    }

    function startAuto() {
      autoSlide = setInterval(nextSlide, 3000);
    }

    indicators.forEach(dot => {
      dot.addEventListener('click', () => {
        clearInterval(autoSlide);
        showSection(parseInt(dot.dataset.index));
        startAuto();
      });
    });

    // Start
    showSection(0);
    startAuto();

  // Navbar active link highlight
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach(link => {
    // Agar current URL me link ka href match kare to active kar do
    if (link.href === window.location.href) {
      link.classList.add("active");
    } else {
      link.classList.remove("active");
    }
  });
// hotels logic
document.addEventListener('DOMContentLoaded', function() {
            const cards = document.querySelectorAll('.scard');
            
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-10px)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });
        });