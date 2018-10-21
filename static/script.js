var subjectGroups = ['ISTQB','CAN','OOP','Personal','Logic'];

$(document).ready(function(){
    $("#btn_istqb").click(function(){
        for (var i = 0; i < 5; i++){
            var classToHide = '.' + subjectGroups[i];
            $(classToHide).hide();        
        }
        $('.ISTQB').show();   
    });
});

$(document).ready(function(){
    $("#btn_can").click(function(){
        for (var i = 0; i < 5; i++){
            var classToHide = '.' + subjectGroups[i];
            $(classToHide).hide();        
        }
        $('.CAN').show();   
    });
});

$(document).ready(function(){
    $("#btn_oop").click(function(){
        for (var i = 0; i < 5; i++){
            var classToHide = '.' + subjectGroups[i];
            $(classToHide).hide();        
        }
        $('.OOP').show();   
    });
});

$(document).ready(function(){
    $("#btn_logic").click(function(){
        for (var i = 0; i < 5; i++){
            var classToHide = '.' + subjectGroups[i];
            $(classToHide).hide();        
        }
        $('.Logic').show();   
    });
});

$(document).ready(function(){
    $("#btn_personal").click(function(){
        for (var i = 0; i < 5; i++){
            var classToHide = '.' + subjectGroups[i];
            $(classToHide).hide();        
        }
        $('.Personal').show();   
    });
});

$(document).ready(function(){
    $("#btn_all").click(function(){
        for (var i = 0; i < 5; i++){
            var classToShow= '.' + subjectGroups[i];
            $(classToShow).show();        
        }
    });
});

