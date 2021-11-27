var currentPage = 1;
var navbarTexts = ['Menu', 'Home', 'About', 'Projects', 'Q&A', 'Contact'];
var isLargeScreen = window.matchMedia('(min-width: 992px)').matches;

$(function() {
    $(window).resize(function() {
        isLargeScreen = window.matchMedia('(min-width: 992px)').matches;
        updateBars();
    });

    $('.navbar, #navbarNav').on('scroll touchmove mousewheel', function(e) {
        e.preventDefault();
        e.stopPropagation();
        return false;
    })

    $('#fullpage').fullpage({
        scrollingSpeed: 300,
        autoScrolling: false,
        fitToSection: false,
        verticalCentered: false,
        onLeave: function(origin, destination, direction) {
            currentPage = destination;
            $('.sidebar-before').show();
            $('.sidebar-after').hide();
            $('.sidebar-after-' + currentPage).show();
            $('.sidebar-before-' + currentPage).hide();

            $('.navbar-before').show();
            $('.navbar-after').hide();
            $('.navbar-after-' + currentPage).show();
            $('.navbar-before-' + currentPage).hide();
            updateBars();
        }
    });

    $('.navbar-fb').hover(function() {
        $('.navbar-before-fb').hide();
        $('.navbar-after-fb').show();
    }, function() {
        $('.navbar-after-fb').hide();
        $('.navbar-before-fb').show();
    });

    $('.navbar-ig').hover(function() {
        $('.navbar-before-ig').hide();
        $('.navbar-after-ig').show();
    }, function() {
        $('.navbar-after-ig').hide();
        $('.navbar-before-ig').show();
    });

    $('.sidebar-fb').hover(function() {
        $('.sidebar-before-fb').hide();
        $('.sidebar-after-fb').show();
    }, function() {
        $('.sidebar-after-fb').hide();
        $('.sidebar-before-fb').show();
    });

    $('.sidebar-ig').hover(function() {
        $('.sidebar-before-ig').hide();
        $('.sidebar-after-ig').show();
    }, function() {
        $('.sidebar-after-ig').hide();
        $('.sidebar-before-ig').show();
    });
});

function toggleNavbar() {
    if ($('#navbarToggler').hasClass('fa-grip-lines')) {
        openNavbar();
    } else {
        closeNavbar();
    }
}

function openNavbar() {
    $('#navbarText').text(navbarTexts[0]);
    $('#navbarToggler').removeClass('fa-grip-lines').addClass('fa-times');
    $('#navbarNav').show();
}

function closeNavbar() {
    $('#navbarText').text(navbarTexts[currentPage]);
    $('#navbarToggler').removeClass('fa-times').addClass('fa-grip-lines');
    $('#navbarNav').hide();
}

function movePage(destination) {
    $.fn.fullpage.moveTo(destination);
    closeNavbar();
}

function updateBars() {
    if (isLargeScreen) {
        closeNavbar();
        $('.navbar').hide();
        if (currentPage > 1) {
            $('#sidebar').show();
        } else {
            $('#sidebar').hide();
        }
    } else {
        $('#sidebar').hide();
        if (currentPage > 1) {
            $('.navbar').show();
        } else {
            $('.navbar').hide();
        }
        if ($('#navbarText').text() !== navbarTexts[0]) {
            $('#navbarText').text(navbarTexts[currentPage]);
        }
    }
}
