//let persona3 = new Persona('Carla','Ponce'); esto no se debe hacer: persona is not defined
                                                //no se puede hacer HOSTING

class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }   

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

}

class Empleado extends Persona{ // clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Nicolás','Bogado');
persona1.nombre = 'Juan Carlos';
persona1.apellido = 'Gomez';
//console.log(persona1);
let persona2 = new Persona('Pedro','Díaz')
persona2.nombre = 'María Laura';
persona2.apellido = 'Gonzales';
//console.log(persona2);

console.log(persona1.nombre); // accedemos a través del get
console.log(persona2.nombre);
console.log(persona1.apellido);
console.log(persona2.apellido);

let empleado1 = new Empleado('María', 'Gimenez', 'sistemas');
console.log(empleado1);
console.log(empleado1.nombre);
