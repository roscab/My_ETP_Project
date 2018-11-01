
var isSelected = {};

$(document).ready(function(){
    $(".btn").click(function(){    
            var questionType = $(this).attr("tag");

            $(".question").each(function( index ) {
                $(this).hide();
              });  
            $(".question").each(function( index ) {
                if($(this).attr("tag") ==  questionType)
                     $(this).show();
              });        
    });
});

$(document).ready(function(){
    $("#btn_all").click(function(){            
            $(".question").each(function( index ) {
                $(this).show();
              });     
    });
});

$(document).ready(function(){
    $("#btn_selected").click(function(){            
            $(".question").each(function( index ) {
                if ($($(this).children()).is(":checked")){
                    $(this).show();    
                }
              });     
    
    });
});

$(document).ready(function(){
    $("#btn_report").click(function(){
        $(".question").each(function( index ) {
            var id = $(this).children().attr("id");
            $(this).hide();
            if ($($(this).children()).is(":checked")){
                isSelected [id] = true;
            }     
            else
            {
                isSelected [id] = false;
            }     
        });   

        $("table").each(function( index ) {
            $(this).show();
        });  

        $(".entry").each(function( index ) {
            if( isSelected[ $(this).attr("id")] == true )
            $(this).show();
        });  
        $(".sidebar").hide();   
        $(".header").hide(); 
        $(".questions_chategory").hide();
        $(".questions").hide();
        $("#btn_report").hide();
        $("#btn_print").show();
        $(".btn_print").show();
    });
});

$(document).ready(function(){
    $("#btn_print").click(function(){      
        $(".candidate").show(); 
        $("#btn_print").hide(); 
        $("#btn_home").hide();
        window.print();
        $("#btn_print").show();
        $("#btn_home").show(); 
        $(".candidate").hide();
    });
});

