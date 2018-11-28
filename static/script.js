
var isSelected = {};

// on page load execute below instructions
$( document ).ready(function() {
         
    $(".status").each(function( index ) {
        var status = $(this).text();
        if (status.includes("Pass"))
            $(this).css("color", "#055B14")  
        else
            if (status.includes("Rejected by"))
                $(this).css("color", "#5B0505")    
            else    
                if (status.includes("pending"))
                    $(this).css("color", "#E39728")    
                else           
                    $(this).css("color", "#05125B") // this color is set for candidates that reject the offer                
    });  

    // shows the technical feedback icon for entrys that don`t have it
    $(".tech_feedback_icon").each(function( index ) {
        var feedback = $(this).attr("data-content");
        if (!feedback.includes("no info") && !feedback.includes("Pending"))
            $(this).css("visibility", "visible");
    });    
    
    // shows the technical date icon for entrys that don`t have it or have it as default
    $(".tech_feedback_date_icon").each(function( index ) {
        var date = $(this).attr("data-content");
        if (!date.includes("None") && date!="Jan. 1, 2000")  
            $(this).css("visibility", "visible");
    }); 
    
    // shows the bul feedback icon for entrys that don`t have it
    $(".bul_feedback_icon").each(function( index ) {
        var feedback = $(this).attr("data-content");
        if (!feedback.includes("no info") && !feedback.includes("Pending"))
            $(this).css("visibility", "visible");
    });    
    
    // shows the bul date icon for entrys that don`t have it or have it as default
    $(".bul_feedback_date_icon").each(function( index ) {
        var date = $(this).attr("data-content");
        if (!date.includes("None") && date!="Jan. 1, 2000")  
            $(this).css("visibility", "visible");
    });   
    
    
    // shows the contact icon for entrys that don`t have it or have it as default
    $(".contact_icon").each(function( index ) {
    var date = $(this).attr("data-content");
    if (!date.includes("not available"))  
        $(this).css("visibility", "visible");
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

$(document).ready(function(){
    $("#btn_cancel_bul_feedback").click(function(){  
        $("#container_new_bul_report").css("visibility", "hidden");
        location.reload();
    });
});

$(function () {
    $('[data-toggle="popover"]').popover()
})
