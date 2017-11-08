"use strict";
  
// After page load, get the pokemons. 

    $(document).ready(function(){ 
        getPokes();                

    }); 

// get pokemon function and load first pokemon
        function getPokes(){
            // Get the pokemon by adding HTML to the div pokearea.
            for(var pokeid = 1; pokeid <= 151; pokeid++){
                $("#pokearea").append("<img id=pokeID"+pokeid+" pokeID='"+pokeid+"' src='http://pokeapi.co/media/img/"+pokeid+".png' alt='Pokemon # "+pokeid+" from pokeapi.com'>");
            }
                var thispokeid = 1;
                $.get("http://pokeapi.co/api/v1/pokemon/"+thispokeid+"/", function(pokeinfo) {
                var thispokename = pokeinfo.name;
                $("#pokename").append("<h2>"+pokeinfo.name+"</h2>");
                $("#mainpokeimage").attr("src","http://pokeapi.co/media/img/"+thispokeid+".png");
                for(var i = 0; i < pokeinfo.types.length; i++){
                    $("#poketypes").append("<li>"+pokeinfo.types[i].name+"</li>");
                    };
                $("#height").append("<p>"+pokeinfo.height+"</p>");
                $("#weight").append("<p>"+pokeinfo.weight+"</p>");
                for(var i = 0; i < pokeinfo.abilities.length; i++){
                    $("#abilities").append("<p>"+pokeinfo.abilities[i].name+"</p>");
                    };
                $("#attackdefense").append("<p>"+pokeinfo.attack+" | "+pokeinfo.defense+"</p>");
                }, "json");                
            };

// on clicking one of the pokemon, update the DOM html to show the info on the pokemon in the red box.  

        $(document).on("click", "img", function(){ 

// get the pokeid from the html that already loaded with getPokes()

            var thispokeid = $(this).attr("pokeid");

// contact the API to get information for the clicked poke.

            $.get("http://pokeapi.co/api/v1/pokemon/"+thispokeid+"/", function(pokeinfo) {

// use the API info to populate the information box. 

            var thispokename = pokeinfo.name;
            $("h2").remove;    // why is this line not working? AHHHHHHHHHHHH.
            $("#pokename").append("<h2>"+pokeinfo.name+"</h2>");
            $("#mainpokeimage").attr("src","http://pokeapi.co/media/img/"+thispokeid+".png");
            for(var i = 0; i < pokeinfo.types.length; i++){
                $("#poketypes").append("<li>"+pokeinfo.types[i].name+"</li>");
            }
            $("#height").append("<p>"+pokeinfo.height+"</p>");
            $("#weight").append("<p>"+pokeinfo.weight+"</p>");
            for(var i = 0; i < pokeinfo.abilities.length; i++){
                console.log(pokeinfo.abilities[i].name);
                $("#abilities").append("<p>"+pokeinfo.abilities[i].name+"</p>");
            }
            $("#attackdefense").append("<p>"+pokeinfo.attack+" | "+pokeinfo.defense+"</p>");
            }, "json");                
        });