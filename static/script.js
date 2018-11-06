
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

$( document ).ready(function() {
    $(".status").each(function( index ) {
        var status = $(this).text();

        switch ($.trim(status)) { 
            case 'In process': 
                $(this).css("color", "#F3A712");  
                break;
            case 'Pass all process': 
                $(this).css("color", "#46A667");         
                break;
            case 'Stand by': 
                $(this).css("color", "#2CED1A"); 
                break;
            case 'Rejected technical interview': 
                $(this).css("color", "#D62828");  
                break;    
            case 'Rejected by recruiter':
                $(this).css("color", "#640D14");  
                break;  
            case 'Rejected by BUL': 
                $(this).css("color", "#960200");  
                break;  
            case 'Rejected by BUL/Client': 
                $(this).css("color", "#960200");  
                break;   
            case 'Rejected by client': 
                $(this).css("color", "#960200");  
                break;        
            case 'Rejected pre-offer': 
                $(this).css("color", "#4392F1");  
                break;        
            case 'Rejected offer': 
                $(this).css("color", "#0E427A");  
                break;                  
            default:
                $(this).css("color", "Black");  
        }
     });  
});


$(document).ready(function(){
    $(".btn").click(function(){    
            var candidateType = $(this).attr("tag");

            $(".candidate_entry").each(function( index ) {
                $(this).hide();
              });  
            $(".candidate_entry").each(function( index ) {
                if(candidateType == 'all')
                    $(this).show();
                else    
                    if($(this).attr("tag") ==  candidateType)
                        $(this).show();
              });        
    });
});
