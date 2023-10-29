$().ready(function() {
    var ads = window.location.pathname;
    var pagename = ads.substr(1).split('.')[0];
    if (pagename == 'research') {
        $('#researchnav').addClass('active');
    }
    else if (pagename == 'blog') {
        $('#publicationsnav').addClass('active');
    }
    // else if (pagename == 'tabs') {
    //     $('#literaturenav').addClass('active');
    // }
});