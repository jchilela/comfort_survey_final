function ocupant_ident_save(){
                    var age= document.getElementById("age").value;
                    localStorage.setItem('age', age);
                    var gender= document.getElementById("gender").value;
                    localStorage.setItem('gender', gender);
                    var weight= document.getElementById("weight").value;
                    localStorage.setItem('weight', weight);
                var username = "$context.username";
                }
function ocupant_ident_set(){
        var age = localStorage.getItem('age');
        var gender = localStorage.getItem('gender');
        var weight = localStorage.getItem('weight');
 		document.getElementById("age").value = age;
        document.getElementById("gender").value = gender;
        document.getElementById("weight").value = weight;

}




//GENERAL THERMAL COMFORT

function gen_th_save(){
                    var tcomfort= document.getElementById("tcomfort").value;
                    localStorage.setItem('tcomfort', tcomfort);
					var pref= document.getElementById("pref").value;
					localStorage.setItem('pref', pref);
                    var acept= document.getElementById("acept").value;
                    localStorage.setItem('acept', acept);           
                     var sens= document.getElementById("sens").value;
                    localStorage.setItem('sens', sens);
                    var oba= document.getElementById("oba").value;
                    localStorage.setItem('oba', oba);
                    var atime= document.getElementById("atime").value;
                    localStorage.setItem('atime', atime);
                    var dtime= document.getElementById("dtime").value;
                    localStorage.setItem('dtime', dtime);

alert('saved');

                }

function gen_th_set(){
        var tcomfort=localStorage.getItem('tcomfort');
        var pref= localStorage.getItem('pref');
        var acept= localStorage.getItem('acept');
        var sens= localStorage.getItem('sens');
        var oba= localStorage.getItem('oba');
        var atime= localStorage.getItem('atime');
        var dtime= localStorage.getItem('dtime');

        document.getElementById("tcomfort").value = tcomfort;
        document.getElementById("pref").value = pref;
        document.getElementById("acept").value = acept;
        document.getElementById("sens").value = sens;
        document.getElementById("oba").value = oba;
        document.getElementById("atime").value = atime;

        document.getElementById("dtime").value = dtime;


}
function gen_th_rem(){
        localStorage.removeItem('tcomfort');
        localStorage.removeItem('acept');
        localStorage.removeItem('pref');
        localStorage.removeItem('sens');
        localStorage.removeItem('oba');
        localStorage.removeItem('atime');
        localStorage.removeItem('dtime');
        localStorage.removeItem('age');
        localStorage.removeItem('gender');
        localStorage.removeItem('weight');

}