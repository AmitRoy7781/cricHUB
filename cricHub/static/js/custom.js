$(document).ready(function(){
	"use strict";

	/* 
	==============================================================
			Slick Slider Main Banner Script Start
	============================================================== 
	*/
	if($('.main_banner').length){
		$('.main_banner').slick({
			fade: true
		});
	}

	/*
	==============================================================
	COUNTDOWN  Script Start
	==============================================================
	*/
	if($('.countdown').length){
		$('.countdown').downCount({ date: '8/8/2017 12:00:00', offset: +1 });
	}

	if($('#kf_countdown').length){
		var deadline = new Date(Date.parse(new Date()) + 15 * 24 * 60 * 60 * 1000);
		initializeClock('kf_countdown', deadline);
	}
	/*
	==============================================================
	Counter Script Start
	============================================================== 
	*/
	if($('.counter').length){
		$('.counter').counterUp({
			delay: 20,
			time: 1000
		});
	}
	/*
	=======================================================================
	Tool Tip Script Script
	=======================================================================
	*/
	if($('[data-toggle="tooltip"]').length){
		$('[data-toggle="tooltip"]').tooltip();
	}

	/*
	=======================================================================
	Pretty Photo Script Script
	=======================================================================
	*/
	if($("a[data-rel^='prettyPhoto']").length){
		$("a[data-rel^='prettyPhoto']").prettyPhoto();
	}

	/*
	============================================================== 
	DL Responsive Menu
	============================================================== 
	*/
	if(typeof($.fn.dlmenu) === 'function'){
		$('#kode-responsive-navigation').each(function(){
			$(this).find('.dl-submenu').each(function(){
				if( $(this).siblings('a').attr('href') && $(this).siblings('a').attr('href') !== '#' ){
					var parent_nav = $('<li class="menu-item kode-parent-menu"></li>');
					parent_nav.append($(this).siblings('a').clone());
					$(this).prepend(parent_nav);
				}
			});
			$(this).dlmenu();
		});
	}

	/*
	==============================================================
	SLICK SLIDER 2 WITH NAVIGATION
	==============================================================
	*/
	if($('.slider-for2').length){
		$('.slider-for2').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			dots: true,
			asNavFor: '.slider-nav2'
		});
	}
	if($('.slider-nav2').length){
		$('.slider-nav2').slick({
			slidesToShow: 3,
			slidesToScroll: 1,
			asNavFor: '.slider-for2',
			dots: false,
			vertical: true,
			centerMode: true,
			focusOnSelect: true,
			arrows: false,
			autoplay: false,
			responsive: [
				{
					breakpoint: 992,
					settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
					infinite: true,
					vertical: false,
					dots: true
					}
				},
				{
					breakpoint: 768,
					settings: {
					slidesToShow: 2,
					slidesToScroll: 3,
					vertical: false,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 481,
					settings: {
					slidesToShow: 1,
					vertical: false,
					slidesToScroll:1
					}
				}
				// You can unslick at a given breakpoint now by adding:
				// settings: "unslick"
				// instead of a settings object
			]
		});
	}

	/*
	==============================================================
	SLICK SLIDER 2 WITH NAVIGATION
	==============================================================
	*/
	if($('.slider-for3').length){
		$('.slider-for3').slick({
			slidesToShow: 1,
			slidesToScroll: 1,
			arrows: false,
			fade: true,
			dots: false,
			asNavFor: '.slider-nav3'
		});
	}
	if($('.slider-nav3').length){
		$('.slider-nav3').slick({
			slidesToShow: 4,
			slidesToScroll: 1,
			asNavFor: '.slider-for3',
			dots: false,
			vertical: true,
			centerMode: false,
			focusOnSelect: true,
			arrows: false,
			autoplay: false,
			responsive: [
				{
					breakpoint: 1400,
					settings: {
					slidesToShow: 4,
					slidesToScroll: 1,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 1024,
					settings: {
					slidesToShow: 4,
					slidesToScroll: 3,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 991,
					settings: {
					slidesToShow: 4,
					slidesToScroll:1
					}
				},
				{
					breakpoint: 767,
					settings: {
					slidesToShow: 2,
					vertical: false,
					slidesToScroll: 1
					}
				}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
			]
		});
	}


	/*
	==============================================================
	Fixture SLIDER  Script Start
	==============================================================
	*/
	if($('.fixtures-slider').length){
		$('.fixtures-slider').slick({
			dots: false,
			autoplay: true,
			arrows: false,
			autoplaySpeed: 1000,
			slidesToShow: 6,
			slidesToScroll: 1,
			responsive: [
				{
					breakpoint: 1400,
					settings: {
					slidesToShow: 4,
					slidesToScroll: 4,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 1024,
					settings: {
					slidesToShow: 3,
					slidesToScroll: 3,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 600,
					settings: {
					slidesToShow: 2,
					slidesToScroll: 2
					}
				},
				{
					breakpoint: 480,
					settings: {
					slidesToShow: 1,
					slidesToScroll: 1
					}
				}
				// You can unslick at a given breakpoint now by adding:
				// settings: "unslick"
				// instead of a settings object
			]
		});
	}
	/*
	==============================================================
	BRAND SLIDER  SCRIPT START
	==============================================================
	*/
	if($('.brand_slider').length){
		$('.brand_slider').slick({
			dots: false,
			autoplay: true,
			arrows:false,
			autoplaySpeed: 2000,
			slidesToShow: 5,
			slidesToScroll: 1,
			responsive: [
				{
					breakpoint: 1024,
					settings: {
					slidesToShow: 3,
					slidesToScroll: 1,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 600,
					settings: {
					slidesToShow: 2,
					slidesToScroll: 2
					}
				},
				{
					breakpoint: 480,
					settings: {
					slidesToShow: 1,
					slidesToScroll: 1
					}
				}
				// You can unslick at a given breakpoint now by adding:
				// settings: "unslick"
				// instead of a settings object
			]
		});
	}

	/*
	==============================================================
	Instagram Feed  Script Start
	==============================================================
	*/
	if($('.instagram-feed').length){
		$('.instagram-feed').slick({
			dots: false,
			arrows:false,
			autoplay: true,
			autoplaySpeed: 1000,
			slidesToShow: 6,
			slidesToScroll: 1,
			responsive: [
				{
					breakpoint: 1400,
					settings: {
					slidesToShow: 4,
					slidesToScroll: 4,
					infinite: true,
					dots: false
					}
				},
				{
					breakpoint: 1024,
					settings: {
						slidesToShow: 3,
						slidesToScroll: 3,
						infinite: true,
						dots: false
					}
				},
				{
					breakpoint: 600,
					settings: {
						slidesToShow: 2,
						slidesToScroll: 2
					}
				},
				{
					breakpoint: 480,
					settings: {
						slidesToShow: 1,
						slidesToScroll: 1
					}
				}
				// You can unslick at a given breakpoint now by adding:
				// settings: "unslick"
				// instead of a settings object
			]
		});
	}



	/*
	==============================================================
	ROSTER SLIDER  Script Start
	==============================================================
	*/
	if($('.rgb-recommend-slider').length){
		$('.rgb-recommend-slider').slick({
			dots: false,
			arrows:false,
			autoplay: true,
			autoplaySpeed: 2000,
			slidesToShow: 3,
			slidesToScroll: 1,
			responsive: [
				{
					breakpoint: 1024,
					settings: {
					slidesToShow: 3,
					slidesToScroll: 3,
					infinite: true,
					dots: true
					}
				},
				{
					breakpoint: 600,
					settings: {
					slidesToShow: 2,
					slidesToScroll: 2
					}
				},
				{
					breakpoint: 480,
					settings: {
					slidesToShow: 1,
					slidesToScroll: 1
					}
				}
			// You can unslick at a given breakpoint now by adding:
			// settings: "unslick"
			// instead of a settings object
			]
		});
	}
	/*
	=======================================================================
	Progress Bar
	=======================================================================
	*/
	if($(".progress-bar").length){
		$(".progress-bar").each(function(){
			each_bar_width = $(this).attr('aria-valuenow');
			$(this).width(each_bar_width + '%');
		});
	}

	/*
	=======================================================================
	Map Script
	=======================================================================
	*/
    if($('#map-canvas').length){
		google.maps.event.addDomListener(window, 'load', initialize);
    }

	/*
	==============================================================
	Masonry  Script Start
	==============================================================
	*/
    if ($('.masonry').length) {
        var container = document.querySelector('.masonry');
        var msnry = new Masonry(container, {
            itemSelector: '.masonry-item'
        });

        msnry.on('layoutComplete', function() {

            mr_firstSectionHeight = $('.main-container section:nth-of-type(1)').outerHeight(true);

            // Fix floating project filters to bottom of projects container

            if ($('.filters.floating').length) {
                setupFloatingProjectFilters();
                updateFloatingFilters();
                window.addEventListener("scroll", updateFloatingFilters, false);
            }

            $('.masonry').addClass('fadeIn');
            $('.masonry-loader').addClass('fadeOut');
            if ($('.masonryFlyIn').length) {
                masonryFlyIn();
            }
        });

        msnry.layout();
    }
});	
	/*
	=======================================================================
	 CountDown Clock Script
	=======================================================================
	*/
	function getTimeRemaining(endtime) {
		"use strict";
		var t = Date.parse(endtime) - Date.parse(new Date());
		var seconds = Math.floor((t / 1000) % 60);
		var minutes = Math.floor((t / 1000 / 60) % 60);
		var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
		var days = Math.floor(t / (1000 * 60 * 60 * 24));
		return {
		  'total': t,
		  'days': days,
		  'hours': hours,
		  'minutes': minutes,
		  'seconds': seconds
		};
	}
	/*
	=======================================================================
	 CountDown Clock Script
	=======================================================================
	*/
	function initializeClock(id, endtime) {
		"use strict";
		var clock = document.getElementById(id);
		var daysSpan = clock.querySelector('.days');
		var hoursSpan = clock.querySelector('.hours');
		var minutesSpan = clock.querySelector('.minutes');
		var secondsSpan = clock.querySelector('.seconds');

		function updateClock() {
			var t = getTimeRemaining(endtime);

			daysSpan.innerHTML = t.days;
			hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
			minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
			secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

			if (t.total <= 0) {
				clearInterval(timeinterval);
			}
		}

		updateClock();
		var timeinterval = setInterval(updateClock, 1000);
	}

	
	/*
	=======================================================================
	 Map Custom Style Script Script
	=======================================================================
	*/
	function initialize() {
		"use strict";

		var MY_MAPTYPE_ID = 'custom_style';
		var map;
		var brooklyn = new google.maps.LatLng(-37.825132,144.98378200000002);
		var featureOpts = [
		  {"featureType":"landscape.man_made","elementType":"geometry","stylers":[{"color":"#f7f1df"}]},{"featureType":"landscape.natural","elementType":"geometry","stylers":[{"color":"#d0e3b4"}]},{"featureType":"landscape.natural.terrain","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"poi.business","elementType":"all","stylers":[{"visibility":"off"}]},{"featureType":"poi.medical","elementType":"geometry","stylers":[{"color":"#fbd3da"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#bde6ab"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffe15f"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#efd151"}]},{"featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"road.local","elementType":"geometry.fill","stylers":[{"color":"black"}]},{"featureType":"transit.station.airport","elementType":"geometry.fill","stylers":[{"color":"#cfb2db"}]},{"featureType":"water","elementType":"geometry","stylers":[{"color":"#a2daf2"}]}

		];
		var mapOptions = {
		  zoom: 15,
		  center: brooklyn,
		  mapTypeControlOptions: {
			mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
		  },
		  zoomControl: false,
		  scaleControl: false,
		  scrollwheel: false,
		  disableDoubleClickZoom: true,
		  mapTypeId: MY_MAPTYPE_ID
		};

		map = new google.maps.Map(
		  document.getElementById('map-canvas'),
		  mapOptions
		);

		var styledMapOptions = {
		  name: 'Custom Style'
		};

		var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

		map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
	}

