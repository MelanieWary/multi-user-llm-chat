"""Hardcoded conversations database for chat simulation"""
from typing import List

from api.common.data_models import UserMessage, PayloadAndDbObject


DB_CONV: List[PayloadAndDbObject] = [
    PayloadAndDbObject(
        session_id=1,
        conversation=[
            UserMessage(
                user_id=2,
                message="Good morning, I would like to go to a warm and sunny place in January, what place would you recommend ?"
            ),
            UserMessage(
                user_id=2,
                message="I have a budget of 2000€ and would like to spend 10 days there, I wonder if that would be enough."
            ),
            UserMessage(
                user_id=1,
                message="Good morning Mrs Roberts, I am Tom from the customer service. It depends on several elements, including your departure airport, which the cost of your flight will depend on. I see you live in Biarritz, right?"
            ),
            UserMessage(
                user_id=2,
                message="Yes I live in Biarritz."
            ),
            UserMessage(
                user_id=1,
                message="Thanks. Bob, could you provide me with the mean cost of a flight between Biarritz and the Canary Islands in January?"
            ),
            UserMessage(
                user_id=1,
                message="Would it be ok for you Mrs Roberts ?"
            ),
            UserMessage(
                user_id=2,
                message="Yes it would. But is people nice there?"
            ),
            UserMessage(
                user_id=2,
                message="I can't say, I've never been there."
            ),
            UserMessage(
                user_id=1,
                message="Is there anything I could help you with ?"
            ),
            UserMessage(
                user_id=2,
                message="Yes, I would like to know what kind of activities we could do there. I mean, my husband and our 2 children."
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=2,
        conversation=[
            UserMessage(
                user_id=1,
                message="Good morning! How can I assist you with your travel plans today?"
            ),
            UserMessage(
                user_id=3,
                message="Hi! I'm looking to book a family vacation for next summer. Do you have any recommendations?"
            ),
            UserMessage(
                user_id=1,
                message="Absolutely! Do you have a destination in mind or are you open to suggestions?"
            ),
            UserMessage(
                user_id=3,
                message="We're thinking about beaches or theme parks somewhere warm."
            ),
            UserMessage(
                user_id=1,
                message="Great options include Orlando for theme parks or the Caribbean for beaches. Do you prefer a more relaxed or active holiday?"
            ),
            UserMessage(
                user_id=3,
                message="We'd like a mix of both, some days relaxing and others exploring."
            ),
            UserMessage(
                user_id=1,
                message="Understood. For a mix of relaxation and adventure, I recommend Cancun in Mexico or the Florida Keys. Would you like details on these destinations?"
            ),
            UserMessage(
                user_id=3,
                message="Yes, please. Also, what is the best time to visit these places in summer?"
            ),
            UserMessage(
                user_id=1,
                message="The peak summer months are June to August, which is perfect for beaches but can be busy. Bob can you provide us with more details about Cancun and the Keys destinations?"
            ),
            UserMessage(
                user_id=1,
                message="Would you prefer traveling in early summer or late summer?"
            ),
            UserMessage(
                user_id=3,
                message="Early July might be good for us. Can you tell me about accommodation options?"
            ),
            UserMessage(
                user_id=1,
                message="Certainly. I can recommend family-friendly resorts and hotels with pools and kid-friendly amenities. Do you have a preferred hotel star rating?"
            ),
            UserMessage(
                user_id=3,
                message="Probably 4-star hotels. Also, could you give me an idea of the total costs for flights from New York and hotel stays for about 8 days?"
            ),
            UserMessage(
                user_id=1,
                message="Let me check. Flights from your city to Cancun and Florida are approximately €600 per person round-trip, and hotel packages for 7 nights start at €1500 for a family room."
            ),
            UserMessage(
                user_id=3,
                message="That sounds good. Are there any travel restrictions or requirements we should be aware of?"
            ),
            UserMessage(
                user_id=1,
                message="Currently, both destinations require proof of vaccination or negative COVID-19 tests, and travel insurance is recommended. I will send a detailed list shortly."
            ),
            UserMessage(
                user_id=3,
                message="Thank you! Can I go ahead and book these options?"
            ),
            UserMessage(
                user_id=1,
                message="Yes, I can assist you with the bookings. Shall I proceed with the detailed options and reservation process?"
            ),
            UserMessage(
                user_id=3,
                message="Yes, please. I look forward to finalizing the trip!"
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=3,
        conversation=[
            UserMessage(
                user_id=4,
                message="Hello there! I'm Mario Smith. I'm interested in a honeymoon trip to Europe from Montreal. What destinations would you recommend?"
            ),
            UserMessage(
                user_id=1,
                message="Good afternoon Mr Smith. Europe offers many romantic destinations such as Paris, Venice, and the Greek Islands. Do you have a preferred type of scenery or activity?"
            ),
            UserMessage(
                user_id=4,
                message="We enjoy art, history, and beautiful coastal views."
            ),
            UserMessage(
                user_id=1,
                message="In that case, Paris and Santorini could be ideal. Would you prefer a city-focused trip, a seaside retreat, or a combination of both?"
            ),
            UserMessage(
                user_id=4,
                message="A combination would be perfect. Also, we'd like to travel in September for mild weather."
            ),
            UserMessage(
                user_id=1,
                message="September is a great choice. I will gather options for accommodations, flights, and itineraries in those locations."
            ),
            UserMessage(
                user_id=4,
                message="Great! What is the estimated cost for a two-week honeymoon?"
            ),
            UserMessage(
                user_id=1,
                message="For a 14-day honeymoon with flights, hotels, and some activities, costs typically start around €3000 per person. Would you like me to prepare a detailed quote?"
            ),
            UserMessage(
                user_id=4,
                message="Yes, please. Also, do you offer honeymoon packages that include romantic dinners or guided tours?"
            ),
            UserMessage(
                user_id=1,
                message="Yes, we can include packages with romantic dinners, guided city tours, and even exclusive experiences like boat rides in Santorini."
            ),
            UserMessage(
                user_id=4,
                message="That sounds wonderful. Let's include those options. Can we also arrange airport transfers?"
            ),
            UserMessage(
                user_id=1,
                message="Certainly. I will include airport transfers in your package. Would you like to proceed with the booking now?"
            ),
            UserMessage(
                user_id=4,
                message="Yes, please. I'm excited to finalize everything!"
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=4,
        conversation=[
            UserMessage(
                user_id=1,
                message="Good afternoon! How can I make your travel plans easier today?"
            ),
            UserMessage(
                user_id=5,
                message="Hello! I want to plan a solo trip to Asia, but I'm not sure where to go. Can you suggest some destinations?"
            ),
            UserMessage(
                user_id=1,
                message="Certainly! Countries like Thailand, Vietnam, and Japan are popular for solo travelers. Do you have specific interests like adventure, culture, or relaxation?"
            ),
            UserMessage(
                user_id=5,
                message="I'm interested in culture and street food experiences."
            ),
            UserMessage(
                user_id=1,
                message="In that case, Tokyo and Bangkok are excellent options. Would you like guided tours, culinary experiences, or free exploration?"
            ),
            UserMessage(
                user_id=5,
                message="I prefer guided tours and food experiences. Also, I want to travel in November."
            ),
            UserMessage(
                user_id=1,
                message="November is a good choice; the weather is pleasant. I will look for group tours and local food experiences for those destinations."
            ),
            UserMessage(
                user_id=5,
                message="What are the estimated costs for a 3-week trip?"
            ),
            UserMessage(
                user_id=1,
                message="Estimated costs, including flights, accommodations, tours, and food, start at around €2500. Would you like a detailed itinerary and price breakdown?"
            ),
            UserMessage(
                user_id=5,
                message="Yes, that would be helpful. Also, can you tell me about any travel advisories or vaccination requirements?"
            ),
            UserMessage(
                user_id=1,
                message="Currently, vaccinations for Hepatitis A and B, and Tetanus are recommended. Travel advisories vary, but I will send you the latest updates for your selected countries."
            ),
            UserMessage(
                user_id=5,
                message="Thanks! I think I'm ready to proceed with booking once I review the details."
            ),
            UserMessage(
                user_id=1,
                message="Great! I'll prepare the options and contact you shortly to finalize your arrangements."
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=5,
        conversation=[
            UserMessage(
                user_id=1,
                message="Hello! How can I help you plan your ideal vacation today?"
            ),
            UserMessage(
                user_id=6,
                message="Hi! I want to go on a European river cruise."
            ),
            UserMessage(
                user_id=1,
                message="European river cruises are fantastic. Popular routes include the Danube, Rhine, and Douro. Do you prefer a specific country or route?"
            ),
            UserMessage(
                user_id=6,
                message="We'd like to see Germany, Austria, and Hungary along the Danube."
            ),
            UserMessage(
                user_id=1,
                message="Excellent choice. Cruises usually last between 7 and 14 days. Are you looking for a shorter or longer cruise?"
            ),
            UserMessage(
                user_id=6,
                message="We prefer 10 days. Also, what are the costs involved?"
            ),
            UserMessage(
                user_id=1,
                message="Prices for 10-day Danube river cruises range from €2000 to €3500 per person, including accommodations, meals, and guided tours."
            ),
            UserMessage(
                user_id=6,
                message="And can you arrange transport to and from the cruise departure port?"
            ),
            UserMessage(
                user_id=1,
                message="Certainly. I can include transfers from your hotel to the port. Do you have dates in mind for travel?"
            ),
            UserMessage(
                user_id=6,
                message="We are considering late September or early October."
            ),
            UserMessage(
                user_id=1,
                message="I'll look up the best options available during that period and send you the details."
            ),
            UserMessage(
                user_id=6,
                message="Thank you! Once I review the options, I'll get back to you to book."
            ),
            UserMessage(
                user_id=1,
                message="Sounds good. I'll be here to assist whenever you're ready."
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=6,
        conversation=[
            UserMessage(
                user_id=7,
                message= "Hello, I'm Megan Doe. Thanks for you email"
            ),
            UserMessage(
                user_id=7,
                message= "I was wondering, is there a dentist close to the hotel you booked for us? I'he had toothache lately..."
            ),
            UserMessage(
                user_id=1,
                message= "Good morning Ms Doe. I see your hotel is the Grand Hôtel in Bordeaux. Bob could you find the dentists clinics nearby?"
            ),
            UserMessage(
                user_id=7,
                message= "And do you have any restaurant serving healthy food to recommend? My mother-in-law is on diet"
            ),
            UserMessage(
                user_id=1,
                message= "My wife has recently been there, i'll ask her and let you know."
            ),
            UserMessage(
                user_id=1,
                message= "Anything else I could help you with ? Maybe a list of museums as you love art ?"
            ),
            UserMessage(
                user_id=1,
                message= "Oh thanks !"
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=7,
        conversation=[
            UserMessage(
                user_id=8,
                message="Hi, I am John Bell, I contact you because I think you made a mistake in the train you booked",
            ),
            UserMessage(
                user_id=8,
                message="Hello Mr Bell. I see I booked a train trip from Paris to Brest for May 17th at 08:13 am.",
            ),
            UserMessage(
                user_id=8,
                message="Yes, the thing is, my flight will arrive at 08:05 am, so I clearly won't be able to make it on time and catch my train",
            ),
            UserMessage(
                user_id=1,
                message="Let's check if there are other options",
            ),
            UserMessage(
                user_id=1,
                message="Bob, could you tell me what are available train trips from Paris to Brest, for May 17th, after 9 am",
            ),
            UserMessage(
                user_id=8,
                message="I am not sure... What are the next ones?",
            ),
            UserMessage(
                user_id=8,
                message="hmm... I'll actually take the first, I think that will do. ",
            ),
            UserMessage(
                user_id=1,
                message="Ok, I see there are seats available, I'll change your former trip for this one, at no cost.",
            ),
            UserMessage(
                user_id=8,
                message="Great, thanks a lot! Have a nice day ! ",
            ),
            UserMessage(
                user_id=1,
                message="My pleasure. Have a nice day too Mr Bell !",
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=8,
        conversation=[
            UserMessage(
                user_id=9,
                message="Hi, I am Amanda Laurens, I would like to know if you have feedback from customers who previsouly made a similar trip to us to the Canary Isalnds ?",
            ),
            UserMessage(
                user_id=1,
                message="Hello Mrs Laurens. I will send you the information by email right away",
            ),
            UserMessage(
                user_id=1,
                message="Is there anything else I could help you with ?",
            ),
            UserMessage(
                user_id=9,
                message="Yes, I was wondering how is the weather there in July, is it much rainy?",
            ),
            UserMessage(
                user_id=9,
                message="And what's the kind of food we eat?",
            ),
            UserMessage(
                user_id=1,
                message="Mrs Laurens have you already tried empanadas?",
            ),
            UserMessage(
                user_id=9,
                message="Yes I love them, my favorite are tuna. What about you?",
            ),
            UserMessage(
                user_id=1,
                message="I love them very much too! My favorite are beef meat. You will se there are plenty types in the Canary Islands !",
            ),
            UserMessage(
                user_id=9,
                message="Thanks for all this information, bye !",
            ),
            UserMessage(
                user_id=1,
                message="You're welcome, we are here for that. Have a nice evening, and a nice trip if we don't contact each other in the meantime !",
            ),
        ]
    ),
    PayloadAndDbObject(
        session_id=9,
        conversation=[
            UserMessage(
                user_id=10,
                message="Hello Tom, we've just come back from our trip to Australia, and we're not happy, that was awfull !",
            ),
            UserMessage(
                user_id=1,
                message="Hello Mr Memphis. Oh no, I'm sorry to hear that, what did go wrong?",
            ),
            UserMessage(
                user_id=10,
                message="We spent more than twice the budget we planned together.",
            ),
            UserMessage(
                user_id=10,
                message="Meals were 50 AUD on average.",
            ),
            UserMessage(
                user_id=10,
                message="Once I had a coffee for 10 AUD !",
            ),
            UserMessage(
                user_id=1,
                message="Mr Memphis, I'm deeply sorry about that, that seems quite expensive indeed, is that possible you ended up in too luxury restaurants and coffee bars?",
            ),
            UserMessage(
                user_id=10,
                message="Well there were little choice around the InterContinental and we did not know !",
            ),
            UserMessage(
                user_id=10,
                message="Also, my kid James got arrested because he because he threw chewing gum on the ground.",
            ),
            UserMessage(
                user_id=10,
                message="Do you think it's normal?",
            ),
            UserMessage(
                user_id=1,
                message="That seems harsh indeed. Bob can you tell us what is the regulation on garbage thrown on the ground?",
            ),
            UserMessage(
                user_id=10,
                message="And lastly... well there are plenty of things, I can't describe them all, but the last terrible and worst thing was that my wife got bitten by a poisonous snake, we had to go to the hospital, and thank God she was fine after 10 days, but we had to stay there 8 extra days, and our travel insurance did not cover the hopital or the extra days expenses !",
            ),
            UserMessage(
                user_id=10,
                message="I want a refund !",
            ),
            UserMessage(
                user_id=1,
                message="Oh that's terrible for your wife, I'm glad she is ok. Unfortunately we provide you with the brochure detailing all the available travel insurance options, and against my advice, you chose the lowest... So, although I'm sorry and would like to have a solution, I'm afraid you can't get a refund.",
            ),
        ]
    ),
]