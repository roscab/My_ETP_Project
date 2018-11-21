
var isSelected = {};

// on page load execute below instructions
$( document ).ready(function() {
    
    $("#icon_462").css("visibility", "visible");
    $("#date_462").css("visibility", "visible");
     
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
        $("#go_btn_home").hide(); 
        window.print();
        $("#btn_print").show(); 
        $("#go_btn_home").show(); 
        $(".candidate").hide();
        
    });
});


$(document).ready(function(){
    $(".btn").click(function(){    
        console.log($(this).attr("id"));
        if($(this).attr("id") != 'btn_add_candidate' && $(this).attr("id") != 'btn_cancel_entry'){

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
        }      
    });
});

$(document).ready(function(){
    $(".tech_feedback_icon").click(function(){    
        var popup = document.getElementById("popup_feedback_462");
        popup.classList.toggle("show");
    });
});

$(document).ready(function(){
    $(".tech_feedback_date_icon").click(function(){    
        var popup = document.getElementById("popup_feedback_date_462");
        popup.classList.toggle("show");
    });
});

$(document).ready(function(){
    $(".close_popup").click(function(){    
        var popup = document.getElementById("popup_feedback_462");
        popup.classList.toggle("show");
    });
});

$(document).ready(function(){
    $(".close_popup_date").click(function(){    
        var popup = document.getElementById("popup_feedback_date_462");
        popup.classList.toggle("show");
    });
});

$(document).ready(function(){
    $("#btn_add_candidate").click(function(){  
        $("#btn_add_candidate").hide()
        $("#new_candidate_window").css("visibility", "visible");
    });
});

$(document).ready(function(){
    $("#btn_cancel_entry").click(function(){  
        $("#new_candidate_window").css("visibility", "hidden");
        $("#btn_add_candidate").show()
    });
});


// check if the tow can be merged 

$(document).ready(function(){
    $("#btn_cancel_technical_feedback").click(function(){  
        $("#container_new_technical_report").css("visibility", "hidden");
        location.reload();
    });
});

$(document).ready(function(){
    $("#btn_cancel_bul_feedback").click(function(){  
        $("#container_new_bul_report").css("visibility", "hidden");
        location.reload();
    });
});

function addTehcnicalReport() {
    $("#container_new_technical_report").css("visibility", "visible");
    var entry_id = event.target.id
    $('#entry_id_field_tech').attr('value',entry_id);
}

function addBulReport() {
    $("#container_new_bul_report").css("visibility", "visible");
    var entry_id = event.target.id
    $('#entry_id_field_bul').attr('value',entry_id);
}
    