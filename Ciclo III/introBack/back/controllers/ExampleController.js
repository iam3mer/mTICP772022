module.exports = class ExampleController {

  static async entrada (request, response) {
    response.send("Acabas de hacerme una solicitud!");
  }

  static async saludar (request, response) {
    response.status(200).json({saludo: "Hola Tripulantes!"});
  }

}