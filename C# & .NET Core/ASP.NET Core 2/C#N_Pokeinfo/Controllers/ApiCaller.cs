using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Collections.Generic;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace pokeinfo
{
    public class WebRequest
    {
        public static async Task GetPokemonDataAsync(int PokeId, Action<Pokemon> Callback)
        {
            // Create a temporary HttpClient connection.
            using (var Client = new HttpClient())
            {
                try
                {
                    Client.BaseAddress = new Uri($"http://pokeapi.co/api/v2/pokemon/{PokeId}");
                    HttpResponseMessage Response = await Client.GetAsync(""); // Make the actual API call.
                    Response.EnsureSuccessStatusCode(); // Throw error if not successful.
                    string StringResponse = await Response.Content.ReadAsStringAsync(); // Read in the response as a string.
                    
                    JObject PokeObject = JsonConvert.DeserializeObject<JObject>(StringResponse);
                    
                    JArray TypeList = PokeObject["types"].Value<JArray>();

                    List<string> Types = new List<string>();

                    foreach(JObject TypeObject in TypeList)
                    {
                        Types.Add(TypeObject["type"]["name"].Value<string>());
                    }

                    Pokemon PokeData = new Pokemon{
                        Name = PokeObject["name"].Value<string>(),
                        Weight = PokeObject["weight"].Value<long>(),
                        Height = PokeObject["height"].Value<long>(),
                        Types = Types

                    };
                     
                    // Finally, execute our callback, passing it the response we got.
                    Callback(PokeData);
                }
                catch (HttpRequestException e)
                {
                    // If something went wrong, display the error.
                    Console.WriteLine($"Request exception: {e.Message}");
                }
            }
        }
    }
}