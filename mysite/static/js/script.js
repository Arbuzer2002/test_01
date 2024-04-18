(function ($) {

  "use strict";

  // init jarallax parallax
  let initJarallax = function () {
    jarallax(document.querySelectorAll(".jarallax"));
    jarallax(document.querySelectorAll(".jarallax-img"), {
      keepImg: true,
    });
  };

  // input spinner
  let initProductQty = function(){

    $('.product-qty').each(function(){

      let $el_product = $(this);

      $el_product.find('.quantity-right-plus').click(function(e){
          e.preventDefault();
          let quantity = parseInt($el_product.find('.quantity').val());
          $el_product.find('.quantity').val(quantity + 1);
      });

      $el_product.find('.quantity-left-minus').click(function(e){
          e.preventDefault();
          let quantity = parseInt($el_product.find('.quantity').val());
          if(quantity > 0){
            $el_product.find('.quantity').val(quantity - 1);
          }
      });

    });

  };

  // init Chocolat light box
  let initChocolat = function () {
    Chocolat(document.querySelectorAll('.image-link'), {
      imageSize: 'contain',
      loop: true,
    });
  };

  // Animate Texts
  let initTextFx = function () {
    $('.txt-fx').each(function () {
      let $this = $(this);
      let words = $this.text().split(' ');
      let newHtml = '';
      $.each(words, function (i, word) {
        newHtml += '<span class="word">';
        $.each(word.split(''), function (j, letter) {
          newHtml += '<span class="letter">' + letter + '</span>';
        });
        newHtml += '</span>';
        if (i < words.length - 1) {
          newHtml += '<span class="letter">&nbsp;</span>';
        }
      });
      $this.html(newHtml);
    });
  };

  $(document).ready(function () {

    initProductQty();
    initJarallax();
    initChocolat();
    initTextFx();

    $(".user-items .search-item").click(function () {
      $(".search-box").toggleClass('active');
      $(".search-box .search-input").focus();
    });
    $(".close-button").click(function () {
      $(".search-box").toggleClass('active');
    });

    let breakpoint = window.matchMedia('(max-width:61.93rem)');

    if (breakpoint.matches === false) {

      let swiperMain = new Swiper(".main-swiper", {
        slidesPerView: 1,
        spaceBetween: 48,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        breakpoints: {
          900: {
            slidesPerView: 2,
            spaceBetween: 48,
          },
        },
      });

      // homepage 2 slider
      let swiperThumb = new Swiper(".thumb-swiper", {
        direction: 'horizontal',
        slidesPerView: 6,
        spaceBetween: 6,
        breakpoints: {
          900: {
            direction: 'vertical',
            spaceBetween: 6,
          },
        },
      });

      let swiperLarge = new Swiper(".large-swiper", {
        spaceBetween: 48,
        effect: 'fade',
        slidesPerView: 1,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        thumbs: {
          swiper: swiperThumb,
        },
      });

    }

    // product single page
    let thumbSlider = new Swiper(".product-thumbnail-slider", {
      slidesPerView: 5,
      spaceBetween: 10,
      // autoplay: true,
      direction: "vertical",
      breakpoints: {
        0: {
          direction: "horizontal"
        },
        992: {
          direction: "vertical"
        },
      },
    });

    // product large
    let largeSlider = new Swiper(".product-large-slider", {
      slidesPerView: 1,
      // autoplay: true,
      spaceBetween: 0,
      effect: 'fade',
      thumbs: {
        swiper: thumbSlider,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

  }); // End of document ready

  $(window).on('load', function(){
    $('.preloader').fadeOut();
  });

})(jQuery);
