#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use Text::CSV;
use Encode qw(encode decode);


my $cgi = CGI->new;
my $Busqueda =uc($cgi-> param('Busqueda por seleccion'))|| '';
my $solicitud =uc($cgi-> param('linkArchivo'));
print $cgi->header(-type => 'text/html', -charset => 'latin-1');
print $cgi->start_html('Leer Archivo CSV');
my $csv_file = 'C:\Users\lenovo\Downloads\Programas de Universidades_4 (1).csv';
my $csv = Text::CSV->new ({ binary => 1, auto_diag => 1, sep_char => '|'});
open my $archivo, '<:encoding(latin-1)', $csv_file or die "Programas de Universidades_4(1).csv: $!";


my $header = $csv->getline($archivo);
my @resultados;
while(my $fila = $csv->getline($archivo)){
    my %datos;
    @datos{@$header} = @$fila;
    if (
        $datos{'NOMBRE'} eq $solicitud ||
        $datos{'PERIODO_LICENCIAMIENTO'} eq $solicitud ||
        $datos{'DEPARTAMENTO_LOCAL'} eq $solicitud ||
        $datos{'DENOMINACION_PROGRAMA'} eq $solicitud
    ) {
        if($datos{'NOMBRE'} ne ''){
            push @resultados, \%datos;
        }
    
    }
}

# Cerrar el archivo CSV
close $archivo;


print <<HTML;
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="latin-1">
    <title>Resultado de la Consulta</title>
    <link rel="stylesheet" href="../estilos.css">
</head>
<body>
    <div>
        <h1>Resultado de la Consulta</h1>
    </div>
    <div class="cabezera">
        <table  border="1">
            <tr>
                <th >Nombre de Universidad</th>
                <th >Periodo de Licenciamiento</th>
                <th >Departamento </th>
                <th >Denominacion Programa</th>
            </tr>
HTML


foreach my $result (@resultados) {
    print "<tr id ='otrasfila'>";
    print "<td class='columna'>$result->{'NOMBRE'}</td>";
    print "<td class='columna'>$result->{'PERIODO_LICENCIAMIENTO'}</td>";
    print "<td class='columna'>$result->{'DEPARTAMENTO_LOCAL'}</td>";
    print "<td class='ultimac'>$result->{'DENOMINACION_PROGRAMA'}</td>";
    print "</tr>";
}


