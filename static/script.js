
// This needs to be reduced
$(document).ready(function(){
    $("#btn_istqb").click(function(){    
            var questionType = $(this).attr("tag");
            console.log( "button tag=" + questionType );

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
    $("#btn_can").click(function(){    
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
    $("#btn_oop").click(function(){    
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
    $("#btn_logic").click(function(){    
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
    $("#btn_personal").click(function(){    
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

// This needs to be reduced

$(document).ready(function(){
    $("#btn_all").click(function(){            
            $(".question").each(function( index ) {
                $(this).show();
              });     
    });
});

// $(document).ready(function(){
//     var counter = 0;
//     $("#btn_selected").click(function(){            
//             $(".question").each(function( index ) {
//                 $(this).hide();
//               });    
//             $("input").each(function( index ) {
//                 if ($($(this)).is(":checked")) 
//                  counter++;
//                  $(this).parent().show();
//               });     
//               console.log ( "selected=" + counter);  
//     });
// });

$(document).ready(function(){
    $("#btn_selected").click(function(){            
            $(".question").each(function( index ) {
                $(this).hide();
              });    
            $(".question").each(function( index ) {
                if ($($(this).children()).is(":checked"))
                $(this).show();  
              });     
    });
});