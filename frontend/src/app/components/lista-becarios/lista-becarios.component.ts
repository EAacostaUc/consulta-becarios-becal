import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-lista-becarios',
  templateUrl: './lista-becarios.component.html',
  styleUrls: ['./lista-becarios.component.css']
})
export class ListaBecariosComponent implements OnInit {

  becarios: any[] = [];
  becariosFiltrados: any[] = [];

  becarioSeleccionado: any = null;

  // se inicializan los filtros que agregue
  filtroNombre: string = '';
  filtroApellido: string = '';
  filtroSexo: string = '';
  filtroTipoBeca: string = '';   
  filtroPaisDestino: string = "";


  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:8000/api/becarios/')
      .subscribe(data => {
        this.becarios = data;
        this.becariosFiltrados = [...this.becarios];
      });
  }



  // sirve para el <select> para filtrar (opciones)
  paisesDestino: string[] = [
  "Estados Unidos",
  "España",
  "Reino Unido",
  "Francia",
  "Alemania",
  "Italia"
];




  // funcion donde se revisan las caracteristicas seleccionadas...
  filtrar() {
    // de todos los becarios existentes solo se guarda en becariosFiltrados los que cumplen...
  this.becariosFiltrados = this.becarios.filter(b => {


    // filtros, nombre y apellido, busca "coincidencias"
    const cumpleNombre =
      this.filtroNombre === "" ||
      b.nombres.toLowerCase().includes(this.filtroNombre.toLowerCase());

    const cumpleApellido =
      this.filtroApellido === "" ||
      b.apellidos.toLowerCase().includes(this.filtroApellido.toLowerCase());



    // aca solo se pide igualdad, de acuerdo a la opcion seleccionada
    const cumpleSexo =
      this.filtroSexo === "" ||
      b.sexo.toLowerCase() === this.filtroSexo.toLowerCase();

    const cumpleTipoBeca =
      this.filtroTipoBeca === "" ||
      b.tipo_beca_resumen?.toLowerCase() === this.filtroTipoBeca.toLowerCase();

    const cumplePaisDestino =
      this.filtroPaisDestino === "" ||
      b.pais_destino?.toLowerCase() === this.filtroPaisDestino.toLowerCase();



    return (
      cumpleNombre &&
      cumpleApellido &&
      cumpleSexo &&
      cumpleTipoBeca &&
      cumplePaisDestino
    );
  });
}



// se resetea lo que se ha filtrado
  limpiar() {
    this.filtroNombre = '';
    this.filtroApellido = '';
    this.filtroSexo = '';
    this.filtroTipoBeca = '';
    this.filtroPaisDestino = "";

    this.becariosFiltrados = [...this.becarios];
    this.becarioSeleccionado = null;
  }

  // solo para ver los detalles del becario seleccionado
  verDetalles(becario: any) {
    this.becarioSeleccionado = becario;
  }
}


