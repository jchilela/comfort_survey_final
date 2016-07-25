function load_strategies(){
         document.getElementById("preference").value = localStorage.getItem('pref');
         document.getElementById("preference").style.visibility = "hidden";
        document.getElementById("st1").anchor.href = null;
        document.getElementById("st3").anchor.href = null;


changebarstatus();

    
}



//PROGRESS BAR STRATEGY 1
var progressbar_value = "10";

function changebarstatus(){ 
    //document.getElementById("submit_Value").disabled = true;

    $(function() {
      var conn = new SockJS('http://172.26.50.120:9080/push');

      conn.onmessage = function(e) {
        console.log('Got', e.data);
        var h = document.createElement("H1") 
        var t = document.createTextNode(e.data);
        h.appendChild(t);
        progressbar_value =h.innerHTML;
        //document.body.appendChild(h);
        //document.getElementById("test").value = document.body.innerHTML

        //alert(progressbar_value);
        //localStorage.setItem('loading',  );
        if (progressbar_value < 0){
             document.getElementById("myBar").style.width = (String(0)).concat('%');
            document.getElementById("label").innerHTML = (String(0)).concat('%') ;   

        }
       else{
             document.getElementById("myBar").style.width = (String(progressbar_value)).concat('%');
        document.getElementById("label").innerHTML = (String(progressbar_value)).concat('%') ;
        }

        //Only perform tasks if this condition is fulfilled
        if ((String(progressbar_value)).concat('%') == "100%"){
        document.getElementById("submit_Value").disabled = false;
           
           
        }
        else{
        //document.getElementById("submit_Value").disabled = true;
        }
        
      }
    });

        set_values();
}





"""PROGRESS BAR FOR STRATEGY 2"""
var progressbar_value = "10";

function changebarstatus_st2(){ 
    //document.getElementById("submit_Value").disabled = true;

    $(function() {
      var conn = new SockJS('http://172.26.50.120:9081/push');

      conn.onmessage = function(e) {
        console.log('Got', e.data);
        var h = document.createElement("H1") 
        var t = document.createTextNode(e.data);
        h.appendChild(t);
        progressbar_value =h.innerHTML;
        //document.body.appendChild(h);
        //document.getElementById("test").value = document.body.innerHTML

        //alert(progressbar_value);
        //localStorage.setItem('loading',  );
        if (progressbar_value < 0){
             document.getElementById("myBar").style.width = (String(0)).concat('%');
            document.getElementById("label").innerHTML = (String(0)).concat('%') ;   

        }
       else{
             document.getElementById("myBar").style.width = (String(progressbar_value)).concat('%');
        document.getElementById("label").innerHTML = (String(progressbar_value)).concat('%') ;
        }

        //Only perform tasks if this condition is fulfilled
        if ((String(progressbar_value)).concat('%') == "100%"){
        document.getElementById("submit_Value").disabled = false;
           
           
        }
        else{
        //document.getElementById("submit_Value").disabled = true;
        }
        
      }
    });

        set_values();
}








function set_values(){

        
}

function home(){
        
            window.location = "/st1";
       
}


function strategy1(){
        
            window.location = "/st1";
       
}


function strategy2(){
        //Only perform tasks if this condition is fulfilled
       // if ((String(progressbar_value)).concat('%') == "100%"){
            window.location = "/st2";

        //}
       // else{
        //alert("Please wait. The system is setting up the initial temperature");
       // }
}


function strategy3(){
       //Only perform tasks if this condition is fulfilled
        
            window.location = "/st3";

}

function strategy4(){

            window.location = "/st4";

    


}



function save_all(){




  $(function(){
        var idade = localStorage.getItem('age');
        var gender = localStorage.getItem('gender');
        var weight = localStorage.getItem('weight');
        var atime= localStorage.getItem('atime');
        var dtime= localStorage.getItem('dtime');
        var tcomfort=localStorage.getItem('tcomfort');
        var acept= localStorage.getItem('acept');
        var pref= localStorage.getItem('pref');
        var sens= localStorage.getItem('sens');
        var oba= localStorage.getItem('oba');
    $.ajax({
      type: "POST",
      url: 'http://172.26.50.120/insert_aci.php',
      data: ({idade: idade, gender: gender, weight: weight, atime: atime, dtime: dtime, tcomfort: tcomfort, acept: acept, pref: pref, sens: sens, oba: oba }),
      success: function(data) {
        alert(data);
      }

    });
  });

alert("Saved Survey")


}









