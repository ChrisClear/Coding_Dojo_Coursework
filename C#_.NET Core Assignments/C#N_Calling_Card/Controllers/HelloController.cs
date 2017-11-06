using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
 
namespace YourNamespace.Controllers
{
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("")]
        public string DisplayOptions()
        {
            return "Use the following URL options for the app, /firstname, /lastname, /age, /favcolor. Each will return my info.";
        }
        
        [HttpGet]
        [Route("firstname")]
        public JsonResult DisplayFirstName()
        {
            return Json("Chris");
        }
        [Route("lastname")]
        public JsonResult DisplayLastName()
        {
            return Json("Clear");
        }
        [Route("age")]
        public JsonResult DisplayAge()
        {
            return Json("20");
        }
        [Route("favcolor")]
        public JsonResult DisplayFavColor()
        {
            return Json("Aqua");
        }
        [HttpGet]
        [Route("{firstName}/{lastName}/{age}/{faveColor}")]
        public JsonResult Jsonify(string firstName, string lastName, int age, string faveColor)
        {
          var callCard = new {
            FirstName = firstName,
            LastName = lastName,
            Age = age,
            FaveColor = faveColor
          };
          return Json(callCard);
        }
        [HttpGet]
        [Route("bonus")]
        public IActionResult Index()
        {
            return View();
        }
    }
       
}
