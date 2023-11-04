$().ready(function() {
    var ads = window.location.pathname;
    var pagename = ads.substr(1).split('.')[0];
    // if (pagename == '' || pagename == 'index') {
    //     $('#indexnav').addClass('active');
    // }
    if (pagename == 'research') {
        $('#researchnav').addClass('active');
    }
    else if (pagename == 'publications') {
        $('#publicationsnav').addClass('active');
    }
    // else if (pagename == 'tabs') {
    //     $('#literaturenav').addClass('active');
    // }
});