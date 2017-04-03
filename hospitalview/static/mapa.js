var meses= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    var meses_short=['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun',
        'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'];
    var dias=['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
    var dias_short= ['Dom', 'Lun', 'Mar', 'Mié;', 'Juv', 'Vie', 'Sáb'];
    var dias_min= ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sá'];

    var date = new Date(2014, 4, 10);
    var date2 = new Date(2014, 4, 30);
    var date3 = new Date(2014, 4, 15);

    function initialize() {
        var mapOptions = {
            center: new google.maps.LatLng(-2.1709979,-79.92235920000002),
            zoom: 10
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
        estados = {
            {% for e in status %}
            "{{ e.id }}":{
                "visible": true,
                "estado":"{{e.estado}}",
                "descripcion":"{{e.descripcion}}",
                "foto":"{{e.foto}}",
            }
           {% if not forloop.last %},{% endif %}
        {% endfor %}
        };
            proyectos = {
            {% for p in sectores %}
            "{{ p.id }}": {
                "visible": true,
                "nombre": "{{ p.nombre }}",
                "descripcion": "{{ p.descripcion }}",
                "kml": "{{p.kmz.url}}",

                "inspecciones": [
                    {% for i in inspecciones %}
                    {
                        "descripcion": "{{ i.descripcion }}",
                        //"usuario":"{{ i.usuario.all.0 }}",

                        "usuario":"{{ i.usuario.nombre }}",
                        
                        "fecha_planificada": "{{ i.fecha|date:"U" }}",
                        
                        "imagen": "{{ i.imagen.url }}",
                        "queja": "{{ i.descripcion }}",
                        "stat": "{{ i.estado.estado  }}",
                        "stat_foto": "{{ i.estado.foto  }}",
                        "latitud": {{i.latitud|stringformat:"f"}},
                        "longitud": {{i.longitud|stringformat:"f"}},
                        
                    }{% if not forloop.last %},{% endif %}
                    {% endfor %}
                ]
            }{% if not forloop.last %},{% endif %}
            {% endfor %}
        };
        var proyectoDescripcion = function(p, img,us, stat) {
            var fotos = "<div class='item'>" +
                        "   <img height='100px' src='" + img + "'>" +
                        "</div>";
            var desc = "<h5>"+ us+"</h5>" +
                    "</span>" +"<h5>Status:</h5>"+"<img height='20px' src=/media/" +    stat + ">"+
                    fotos; 
            
            return desc;
        };

        var infowindow = new google.maps.InfoWindow({
            content:'<span id="hook">Hello World!</span>',
            maxWidth: 1000 ,
            maxHeight: 1000
        });
        
        generadoraAbrirInfoWindow = function x(p, img, us, stat) {
            return function() {
                infowindow.setContent(proyectoDescripcion(p, img,us, stat));
                infowindow.open(map,this);
           }
        } 
        markers = [];

        
        showMarkers = function(stat){
            for (var n in proyectos) {
                var p = proyectos[n];
                var icon = "/media/icon/pens.png";
                if ( ! p.visible ) continue;
                for (var j in p.inspecciones){
                    var i =  p.inspecciones[j];
	    if('undefined' !== typeof stat && stat !== i.stat)
		continue;
                    var usuario = i.usuario;
                    var img = i.imagen;
                    var estado = i.stat_foto;
                    var marker = new google.maps.Marker({
                        position: new google.maps.LatLng(i.latitud, i.longitud),
                        map: map,
                        icon: icon,
                        title: i.usuario
                    });

                    google.maps.event.addListener(marker, 'click', generadoraAbrirInfoWindow(p, img, usuario, estado));

                    markers.push(marker);
                }
            }
        }
        showMarkers();

        removeMarkers = function(){
            for ( var i in markers ){
                markers[i].setMap(null);
            }
            markers = []          
        }

        anio = (new Date()).getFullYear();

        $('#zonas button').attr('disabled', false)
        $('#trimestres button').attr('disabled', true)
        $('#selectanio option').attr('disabled', true)

        $("#proyectos span.glyphicon-eye-open").click(function(){
            window.proyecto = $(this).data('proyecto');
            $(this).next().toggleClass('visible');
            proyectos[window.proyecto].visible = !proyectos[window.proyecto].visible
            removeMarkers(); 
            showMarkers();
        })
        
        $("#proyectos a").click(function(){
            $('#trimestres button').attr('disabled', false);
            $('#selectanio select').attr('disabled', false);
            window.proyecto = $(this).data('proyecto');

        })

        $("#selectanio option").click(function(){
            anio = $(this).data('anio');
        })

        $(".activarbtn").click(function() {
            ntrimestre = $(this).text();
            //$('#zonas button').attr('disabled', false)
            $('#ruta').text( window.proyectos[window.proyecto].nombre + '/' + ntrimestre);
            var inicio = anio + ',' + $(this).data('inicio'); 
            var fin = anio + ',' + $(this).data('fin');
        });

$(".estadobtn").click( function(){
    var estado = $(this).data('botones')
                removeMarkers(); 
                showMarkers(estado);
});

    }
$(document).ready(function(e) { initialize() });