import random

# into violet 1st ep
introcrown = [
    'what do you say? what if i ruled the world? - intro: crown',
    'nobody knows - intro: crown',
    'it means nothing to me, it`s invisible, but you \
              know it`s mine - intro: crown',
    'so where do you see yourself? this is the end - intro: crown',
    'i am running for the crown - intro: crown',
    'i keep breathing when you drown - intro: crown',
    'i believe myself, no doubt - intro: crown',
    'my lord, how come i never lost my faith? - intro: crown'
]
ponzona = [
    'purple on the top, purple kiss on bloody top - ponzona',
    'oh bloody top, i`m sitting in my own seat in the end, woo - ponzona',
    'you`ve waited for me for a long time, haven`t you? - ponzona',
    'it`s spreading more and more, i`m holding onto your \
    breath tightly as i color you in (color you in) - ponzona',
    'my poison is in this kiss mark, it`s slowly spreading, making you lose \
    consciousness - ponzona', 'can`t deny this truth, ponzona - ponzona',
    'baby, purple kiss on bloody top - ponzona',
    'the world is colored purple - ponzona',
    'i`ve made you addicted, fall in love (you better know, \
    you better know) - ponzona', 'you can`t escape it - ponzona',
    '(la-la-la-la) shout out loud - ponzona', '(la-la-la-la) louder - ponzona',
    'in this lost world, purple on the top - ponzona',
    'it`s softly spreading, so you can feel it, so my arrow can \
    strongly pierce you - ponzona',
    'i know you want something, in the place you want give me all of you - ponzona',
    'look at my birth, it`s so mystical - ponzona',
    'a criminal with the name of charm - ponzona',
    'follow me without a word, i`ll go bang bang in your heart, \
    shining from head to toe - ponzona', 'purple on the top\n- ponzona',
    'i`m looking for a place that i can shine even more\n- ponzona',
    'as i wander and keep walking, my scent will confuse you\n- ponzona',
    'no one knows that story, fall deep inside to that unknown place\n- ponzona',
    'baby kiss me\n- ponzona',
    'you`re addicted to me, you`ve fallen for me\n- ponzona'
]
canwetalkagain = [
    'i really don`t understand why we`re like this\n- can we talk again',
    'why isn`t it easy to say i`m sorry?\n- can we talk again',
    'it`s fine, no i regret it\n- can we talk again',
    'you`re so bad but you won`t leave my mind\n- can we talk again',
    'what`s clear right now is, i`ve been thinking about you\n- can we talk again',
    'actually, i miss you\n- can we talk again',
    'honestly, i miss you\n- can we talk again',
    'come back again\n- can we talk again',
    'can we talk again? can we try again?\n- can we talk again',
    'if only we could go back, and laugh like we used to\n- can we talk again',
    'once again, love again\n- can we talk again',
    'as if nothing happened, i`m going back to you, back again\n- can we talk again',
    'back to you, back again\n- can we talk again',
    'it`s been more lonely and more miserable that i thought, \
    because your existence was so big\n- can we talk again',
    'i couldn`t get rid of these feelings, so stupid\n- can we talk again',
    'all the times i spent with you, i wish i could forget them\n- can we talk again',
    'i`m acting like it`s no big deal, like nothing happened\n- can we talk again',
    'like i`m calm, but each day is so uncomfortable\n- can we talk again',
    'don`t ever let me go\n- can we talk again',
    'i don`t wanna open my eyes because you`re not next to me\n- can we talk again',
    'you`ve erased all parts of my day\n- can we talk again',
    'again and again, i`m thinking of you, i can`t stop\n- can we talk again',
    'if only i could turn back time and see you\n- can we talk again',
    'i`m getting tired, i`m trapped in the memories\n- can we talk again',
    'i can`t escape, i can`t get out, why?\n- can we talk again',
    'my heart is growing empty\n- can we talk again'
]
skipskip = [
    'who are you to tell me now, everywhere they love me, \
    i know i`m so hot\n- skip skip',
    'wherever they like it, i`m so used to this feeling\n- skip skip',
    'i know, i know i`m a bit dangerous\n- skip skip',
    'i draw closer and farther from this tug-o-war of emotions\n- skip skip',
    'whenever there`s a chance, i don`t give a shh, shh\n- skip skip',
    'you got it, got it, the kind of style i have\n- skip skip',
    'don`t be off guard once you see it\n- skip skip',
    'perhaps we`ll fall in love, you and me\n- skip skip',
    'it might not be easy, and i, i`m something a little different\n- skip skip',
    'the boring ones, skip skip, the good ones, like it\n- skip skip',
    'don`t ever think i`m an easy one, skip! skip!\n- skip skip',
    'it`s on my mind, tap tap, my taste and accent\n- skip skip',
    'don`t hesitate to speak out like it`s too easy\n- skip skip',
    'say your thoughts with confidence, to put my heart \
    in suspense, skip! skip!\n- skip skip',
    'like you won`t fall down, don`t leave me like you like me\n- skip skip',
    'oh, right\n- skip skip', 'why, why are you like this?\n- skip skip',
    'why, why are you trying to act like this?\n- skip skip',
    'i want my style, ma ma my type, like it\n- skip skip',
    'not ma, my type\n- skip skip',
    'the feeling approaches deeper, more digging\n- skip skip',
    'everyday, what caught my eyes? was none other than you, like it!\n- skip skip',
    'i push and sink into this deep well of feelings\n- skip skip',
    'maybe, maybe you, you`ve fallen into me\n- skip skip',
    'you got it, got it\n- skip skip', 'i`ll show my real self\n- skip skip',
    'i know that, don`t be rude\n- skip skip'
]
hello = [
    'the moonlight goes far away, the blue moon covers your side\n- hello',
    'when can i see you and forget my pain?\n- hello',
    'when tonight passes, should i go back to where i was?\n- hello',
    'i try to soothe my frustration, but time is not on my side\n- hello',
    'i`m without you here, a million miles away\n- hello',
    'you`re the only light that shines on my heart\n- hello',
    'hello, i just want to say hello\n- hello',
    'i wanted to see you face-to-face in my fading memories\n- hello',
    'i miss your warm breath embracing me in the dark\n- hello',
    'hello, hello, hello, how are you, are you doing fine?\n- hello',
    'hello, hello, hello, do you hear this song?\n- hello',
    'my hands couldn`t reach, nor the light could see\n- hello',
    'the situation now is holding my wrist\n- hello',
    'again i, we should keep running to hold that light\n- hello',
    'somebody, somebody said they were pretending to laugh, \
    back then, everything was like that\n- hello',
    'baby so much, i miss you\n- hello',
    'the sky is locked in with love\n- hello',
    'we are waiting for the light, in the shadow that wouldn`t last forever\n- hello'
]
myheart = [
    'without any warning (oh na-na-na) feels like i`ve \
    come to a sudden stop (oh na-na-na)\n- my heart skip a beat',
    'feels like i`m gonna get in trouble, i`m getting a \
    feeling\n- my heart skip a beat',
    'tick tock tick tock, it is time, follow me, follow\n- my heart skip a beat',
    'hurry and tell me, stronger than the voices i hear\n- my heart skip a beat',
    'feels like i`m gonna explode, it`s so electric\n- my heart skip a beat',
    'you just need to come to me, don`t mind the other \
    eyes around you\n- my heart skip a beat',
    'trapped in a maze, my head is a mess\n- my heart skip a beat',
    'the world keeps turning and turning, i`m going crazy\n- my heart skip a beat',
    'cut off all your worries, burn it all up\n- my heart skip a beat',
    'the moment i saw you, my heart skip a beat\n- my heart skip a beat',
    'my heart skip a beat, i can`t breathe\n- my heart skip a beat',
    'i`m being pulled to you, i don`t even know myself\n- my heart skip a beat',
    'it`s just my instinct, cause we`re reacting to each other\n- my heart skip a beat',
    'ding dong, i`m here, hello baby\n- my heart skip a beat',
    'you want me like crazy, i`m not just a lady\n- my heart skip a beat',
    'follow me, follow me, fall into me\n- my heart skip a beat',
    'i`m clapping, clap, everyone can see\n- my heart skip a beat',
    'don`t stop me, it won`t work anyway\n- my heart skip a beat',
    'you`ll have to accept it, calmly\n- my heart skip a beat',
    'my heart is racing then stopping, i feel like dying\n- my heart skip a beat',
    'the more it happens, the more i think of you\n- my heart skip a beat',
    'don`t want complicated things now, so please tell me\n- my heart skip a beat',
    'i wanna burn up, so my heart can react again\n- my heart skip a beat',
    'from A to Z\n- my heart skip a beat',
    'hey girls! don`t stop, keep running\n- my heart skip a beat',
    'hot, hot, follow my heart, follow\n- my heart skip a beat',
    'hey boys! don`t stop, keep going up\n- my heart skip a beat',
    'burn up, shout out even louder, holler\n- my heart skip a beat',
    'listen to my heartbeat, it`s burning\n- my heart skip a beat',
    'my heart is shining even brighter right now, \
    dropping, bomb, ho!\n- my heart skip a beat'
]
period = [
    'on the day when everything ended, think about you and me\n- period',
    'i`m embraced by the empty air, oh, it reminds me of you\n- period',
    'on the day when everything started, think about love and you\n- period',
    'burying the beautiful times in photos, i become nostalgic again\n- period',
    'having our own times, is that the answer? i know it can`t be helped\n- period',
    'not love, but a thing called effort\n- period',
    'and i know ain`t no love in me\n- period',
    'layers of excuses pilled up to let you go, and \
    i know ain`t no love in me\n- period',
    'somebody knows, somebody knows, somebody knows\n- period',
    'somebody takes, somebody takes you away\n- period',
    'i wanna hold, i wanna hold, you say goodbye to me\n- period',
    'every word you said keeps hurting my heart even more\n- period',
    'i keep getting down, unfillable loneliness\n- period',
    'as much as it hurts, as much as i wanted you, \
    it gets harder every day, so i pretend like it`s nothing\n- period',
    'pretend like i`m fine, pretend like i`m strong, and live\n- period',
    'when did it become like this?\n- period',
    'the remaining feelings that we`ve used up, i want \
    to go back, i know i can`t help it\n- period'
]
intoviolet_lyrics = random.choice([introcrown, ponzona, canwetalkagain,
                                  skipskip, hello, myheart, period])
# hide & seek 2nd ep
zombie = [
    'zombie-bie-bie-bie (bie-bie-bie-bie-bie-bie-bie) zombie\n- zombie',
    'sweet and cruel, your taste, taste, taste, taste, taste\n- zombie',
    'i can`t hold it in when i see you\n- zombie',
    'cool down, down down (yeah)\n- zombie',
    'i`m gonna surprise you, a shadow secret in play (yeah)\n- zombie',
    'running, running, try running away\n- zombie',
    'hide and seek begins now\n- zombie',
    '(uh) falling deeply, you`re like dipping sauce\n- zombie',
    'beep, beep, this beeping sound, don`t mind that\n- zombie',
    'look at me only, i`m kinda a big deal, catch up\n- zombie',
    'i`m stealing your heart\n- zombie',
    'when your body touches mine, i get languid\n- zombie',
    'wanna do bad things, cute things (oh my!)\n- zombie',
    'you and i, we`re on fire\n- zombie', 'burning up like a fire\n- zombie',
    'tonight, chase me\n- zombie', 'i`ll chase you like a zombie\n- zombie',
    'before the sunrise\n- zombie',
    '(do ya-ya-ya-ya, do ya-ya-ya, we`re birds from the same flock\n- zombie',
    'hide and seek starts on this night\n- zombie',
    '(Brrah) i am one zombie-bie-bie\n- zombie',
    'you are the prey, you`re all i see, see, see\n- zombie',
    'the night just began, it`s a chase until the sun comes up\n- zombie',
    'it`s like i`m dancing, when i`m running to you\n- zombie',
    'warning, warning, i warned you\n- zombie',
    'i`m hungry, hungry, i don`t know when i might bite you (yah)\n- zombie',
    'come gather around here, gather around with our hands together\n- zombie',
    'hide well\n- zombie', 'PURPLE KISS, hide on bloody top\n- zombie'
]
am = [
    'i`m always thinking about you before i go to sleep\n- 2am',
    'what you want? where you at?\n- 2am',
    'time is running out, time is running out\n- 2am',
    'tell `em a, tell `em about it\n- 2am',
    'a piece of paper that i jot down on (pa-ra-ba-bam-bam)\n- 2am',
    'all the signs that i tried to convey, just sending to you\n- 2am',
    'i`m in love with this comfy mood, and i fell for yu\n- 2am',
    'and let it go, let go, i keep thinking of you\n- 2am',
    'all day for you (all day, for you)\n- 2am',
    'to me and you (to me, and you)\n- 2am',
    'i`ll tell you with courage, that i like you\n- 2am',
    'when you smile next to me (when you smile, yeah) \
    i`m so excited, i smiled like that (i smiled, yeah)\n- 2am',
    'if i like you, it`s over, you keep losing my heart\n- 2am',
    'i`m thinking of you, and it was 2 am in the morning again\n- 2am',
    'i just realized that my heart is full of you, and \
    it was already in my mind\n- 2am',
    'stare at me slowly, and i turn more like you\n- 2am',
    'every night and day, i miss you today\n- 2am',
    'if you accidentally opened your eyes, you could breathe freely\n- 2am'
]
pearls = [
    'what are you saying? be honest\n- cast pearls before swine',
    'what are you doing? look me in the eyes\n- cast pearls before swine',
    'i feel like i`m being punished alone, i got burned by the \
    fire called love\n- cast pearls before swine',
    'no more red lies, if you have time for that, just sleep\n- cast \
    pearls before swine', 'i`m seeing it as it is\n- cast pearls before swine',
    'you don`t know the value, just be on your way\n- cast pearls before swine',
    'foolish love hurts\n- cast pearls before swine',
    'i`ve become stronger, take care, bye bye\n- cast pearls before swine',
    'only after the rose tinted glasses come off, now i know \
    (i`m feeling bummed out)\n- cast pearls before swine',
    'tears like jewelry, i don`t need (pass pass)\n- cast pearls before swine',
    'i was too good for you\n- cast pearls before swine',
    'you`re bad, you break my heart\n- cast pearls before swine',
    'i`m hurt like a fool\n- cast pearls before swine',
    'everyday, i delete it without reading, your mail, \
    everyday\n- cast pearls before swine',
    'uh ya, walk away, go away\n- cast pearls before swine',
    'forget, don`t even think about me, because i`m clearly wasted \
    on you, ya\n- cast pearls before swine',
    'your personality is opposite mine, that`s why i was attracted \
    maybe\n- cast pearls before swine',
    'we argued, fought, and got messed up\n- cast pearls before swine',
    'even before the wounds healed, i don`t know i was trying to match \
    you\n- cast pearls before swine',
    'you`ll regret not recognizing my worth\n- cast pearls before swine',
    'don`t you look back\n- cast pearls before swine',
    'i`m gonna kick you away like a ball, stay out of my \
    sight\n- cast pearls before swine',
    '(la la-la-la-la) just play, forget everything\n- cast pearls before swine',
    'enjoy today, go crazy, be even more excited\n- cast pearls before swine',
    'hands up higher, we just go (i`m feeling so bummed out)\n- \
    cast pearls before swine'
]
sowhy = [
    'you stole my heart, i can`t take it back\n- so why',
    'but i don`t want to take it back, take me for what it is, \
    don`t hesitate\n- so why', 'my stolen heart wants you\n- so why',
    'i just took it so what`s the problem?\n- so why',
    'i`m looking for you, running, running, it has been so long\n- so why',
    'it always happened to be like this\n- so why',
    'i tried so many things to fill up this empty day (oh)\n- so why',
    'in the end, i just lost you, but that`s fine\n- so why',
    'you like that too, don`t hesitate, don`t wait\n- so why',
    'come to me quickly, i`m out of breath\n- so why',
    'woah, i still love you\n- so why',
    'oh, you know i`m the one, babe\n- so why',
    'your girl, only one, babe\n- so why',
    'yeah, oh, we got through so why are we wasting time?\n- so why',
    'uh, why do you still keep standing?\n- so why',
    'i like you, the more i see you, the better you know my heart\n- so why',
    'a mind full of love that has fallen in love\n- so why',
    'blow away the loneliness, all the fear, bye bye\n- so why',
    'look around you, i`m not alone, you`re the precious person who told me\n- so why',
    'i tried to soothe my growing heart\n- so why',
    'and thinking about it every night, now it`s filled with days with you\n- so why',
    'day by day, it`s all made by you (oh)\n- so why',
    'i can`t do it anymore, i`ll tell you first (yeah, yeah, yeah, yeah)\n- so why',
    'now i know, i can`t wait any longer\n- so why',
    'when we`re together and when we`re not together, \
    how can something not be hidden\n- so why',
    'i don`t need a push, no thanks\n- so why',
    'i`m a little scared, what do you do?\n- so why',
    'i can only see you today\n- so why'
]
twinkle = [
    'tears, jewels, stars, and you\n- twinkle',
    'the never ending daylight, the moment that-that-that crosses over\n- twinkle',
    'the sunset falls like the tears of the sun, \
    fully embracing you in gold\n- twinkle',
    'i`ll invite you in my dream\n- twinkle',
    'only the two of us here on the blue night, holding hands under \
    the broken starlight\n- twinkle',
    'this trembling i feel staring at you, this feeling that can`t be \
    touched \n- twinkle',
    'jewelry shining in the dark under the sea, i`ll protect your light\n- twinkle',
    '(di-li-da-la-la-la) i send my heart, along the scattering dusty stars\n- twinkle',
    '(da-li-da-la-la-la) shining splendidly\n- twinkle',
    'will you always shine like that? Tears, jewels, stars, you next to me\n- twinkle',
    'and also you\n- twinkle',
    'stop the clock, and make a world just for you and me, \
    no matter how far it is\n- twinkle',
    'i decorate this diary with violet (yeah) with only you, \
    i don`t need anything else\n- twinkle',
    'countless shining lights, you`re the brightest among them\n- twinkle',
    'with our secret dream (shh, ayy) even this moment \
    is about to end again, ayy\n- twinkle',
    'shine on us twinkle (tw-twinkle, tw-twinkle)\n- twinkle',
    'cross over the universe and pray to the stars\n- twinkle',
    'this most precious glittery moment, twinkle\n- twinkle'
]
zzzz = [
    'even if i sleep all day long, i don`t have any thoughts\n- ZzZz',
    'no matter who looks at me, they say i look spaced out these days\n- ZzZz',
    'even if the song i wanted to listen to comes on, \
    even if a drama that i enjoyed watching comes out on TV, \
    i don`t want it no more\n- ZzZz',
    'these days, it all feels the same\n- ZzZz',
    'i`m feeling blue, still blue, i need love, love, love\n- ZzZz',
    'what about you? in this place where the lights are off?\n- ZzZz',
    'livin` in the lonely city, this night is lonely city\n- ZzZz',
    'it becomes my daily life to sigh every day\n- ZzZz',
    'i can`t say anything\n- ZzZz',
    'it feels like i`m trapped in the midst of people\n- ZzZz',
    'it feels like i`m alone on top of the city\n- ZzZz',
    'this night when i can`t sleep, this place is lonely city\n- ZzZz',
    'also, why is my phone zzzz zzzz? sleep all night\n- ZzZz',
    'why is the phone zzzz zzzz? sleep all night\n- ZzZz',
    'ya, in the lonely city\n- ZzZz',
    'ya, i`m tired wandering in the dark\n- ZzZz',
    'this spinning roulette, can you stop it?\n- ZzZz',
    'get me out, i need your touch\n- ZzZz',
    'look in the mirror, i`m alone, i`m a loner\n- ZzZz',
    'even if the scene i wanted to see appears in my dreams, \
    even if i hear the voice i wanted to hear, i don`t want it no more\n- ZzZz',
    'it doesn`t mean much anymore\n- ZzZz',
    'repeating a colorless day, getting dyed black and white\n- ZzZz',
    'your world feels far way, babe\n- ZzZz',
    'today, like yesterday, lonely\n- ZzZz',
    'my city that i`ve gotten used to, you never know, never know\n- ZzZz',
    'again today, i`m...\n- ZzZz',
    'it`s hard to be alone, oh i`m alone\n- ZzZz'
]
hideseek_lyrics = random.choice([zombie, am, pearls, sowhy, twinkle, zzzz])

# my my 1st digital single
mymy = [
    'i`m going to open my, my wishlist\n- my my',
    'don`t be surprised, my christmas wishlist is you\n- my my',
    'i want you, your heart, your love\n- my my',
    'only one thing this winter, it`s you\n- my my',
    'you`re my only wishlist\n- my my',
    'i get lonelier in december for some reason\n- my my',
    'how do you feel? I don`t want this year to just pass like this, no\n- my my',
    'gifts are exchanged every year, aren`t you fed up? need something warmer\n- my my',
    'tell me what you want for me, what do you want?\n- my my',
    'if you hesitate, i`ll open up my, my wishlist first\n- my my',
    'i hope you feel the same way, it`s just my wish\n- my my',
    'i`m waiting for this miraculous drama\n- my my',
    'the white snow is making me more excited\n- my my', 'i miss you\n- my my',
    'aren`t you tired of being alone? want something more fun\n- my my',
    'tell me what you think of me, can`t you tell yet if you`re like that\n- my my',
    'when the first snow falls again, \
    ringing in my ears again (ra-pa-pam-pam)\n- my my',
    'in your arms welcoming this present, you, i want this \
    moment with you to last forever (ra-pa-pam-pam)\n- my my',
    'tell santa i don`t need any gifts, you are my wish \
    (ra-pa-pam-pam, oh, ra-pa-pam-pam)\n- my my'
]
mymy_lyrics = random.choice([mymy])

# memeM 3rd ep
introillusion = [
    'one, two, and four\n- intro: illusion',
    'i`m just clenching my fist, i`m trying not to lose my mind, it \
    settles me down\n- intro: illusion',
    'i can`t get out of this addicting scent, it settles me down\n- intro: illusion',
    'i can`t find it, under my feet\n- intro: illusion',
    'in the deep, it`s not fake\n- intro: illusion',
    'even if you try running away, i`m in your head \
    (na-na-na-na, na-na)\n- intro: illusion',
    'woah-oh-ooh-woah, this is real\n- intro: illusion',
    'illusion, oh, yeah, yeah, yeah\n- intro: illusion',
    'the delusion filling up your head\n- intro: illusion',
    'oh, wow, wow, wow (drippin`, drippin`, feeling down) illusion\n- intro: illusion',
    'the conclusion that lets me breathe, this is real, my way\n- intro: illusion'
]
memem = [
    'i`m not gonna follow what others do, too boring, dang it\n- memeM',
    'whatcha gonna do about it?\n- memeM', 'M.E.M.E.M.E.M.E.M\n- memeM',
    'BAM BAM BAM, stare at me now, look at me now\n- memeM',
    'P.K. STAY TUNE\n- memeM',
    'i`ll play with you till you go crazy, you`ll fall for me\n- memeM',
    'even if you run away, you`ll be wandering around me, i got cha`\n- memeM',
    'doomdoomdoomdoom (doomdoom dooomdoomdooom)\n- memeM',
    'that`s it, good boy, just follow me\n- memeM',
    'i get in your head\n- memeM',
    'you can`t get away from me, as if you`re under a spell\n- memeM',
    'in your head, i go mem, mem, mem\n- memeM',
    'reverse it, it`s still mem, mem, mem\n- memeM',
    '(mem, mem, meme) now this is fun\n- memeM',
    'this is getting fun\n- memeM',
    'i`m in your head, i`ll dive deeper\n- memeM',
    'into your head, i`m in control\n- memeM', 'purple is back \n- memeM',
    'i`m gonna control you\n- memeM', 'look at my eyes, deep inside\n- memeM',
    'out of control (dim)\n- memeM',
    'i should have trapped you, in my head\n- memeM',
    '(danger) even if i draw a line, the stranger keeps coming closer\n- memeM',
    'mmm yummy yummy \n- memeM',
    'it`s the flavor i was wishing for (mem, mem, mem)\n- memeM',
    'sweet like bear, gummy gummy\n- memeM',
    'this presence that drives you mad is fire\n- memeM',
    'i`ll make you swim in the purple world (woa-woo woah)\n- memeM',
    '(woa-a-woo woah)so that i can have you whenever i want\n- memeM',
    'heads, hips, knees, body (mem, mem, mem) shake it all you want\n- memeM'
]
memem_lyrics = random.choice([introillusion, memem])

# geekyland 4th ep
byebyebully = [
    'please, don`t hurt me like that\n- intro: bye bye bully',
    'hey, have you got no shame\n- intro: bye bye bully',
    'you make me cry\n- intro: bye bye bully',
    'get the hell out of my life\n- intro: bye bye bully',
    'i`m still alive, i will be more stronger\n- intro: bye bye bully',
    'ooh bye bye bye bye bye bully\n- intro: bye bye bully',
    'ooh love love love love love me\n- intro: bye bye bully',
    'don`t kill kill kill kill kill me\n- intro: bye bye bully',
    'kiss me, kill me like that\n- intro: bye bye bully',
    'ha ha ha ha ha bye bye bully\n- intro: bye bye bully'
]
nerdy = [
    'my shirt, big size, my hoodie that is a bit loose\n- nerdy',
    'ootd, my circular glasses\n- nerdy',
    'yes, i`m nerd, i`m a stubborn freak, but we`re gonna take it all\n- nerdy',
    'i am somewhere between e and i\n- nerdy',
    'even if i am a loser, i don`t care, so what!?\n- nerdy',
    'waht the hell, like useless hashtag, i don`t need your attention\n- nerdy',
    'guess who? who ignores the world\n- nerdy',
    'even if i am foolish, 5 4 3 i want\n- nerdy',
    'ok i`m nerdy, but i`m not stupid so what (na na ni nanina)\n- nerdy',
    'i love myself\n- nerdy', 'yeah i`m so nerdy, same pretty (no)\n- nerdy',
    'you make fun of me, you make me cool\n- nerdy',
    '(da da da da) bully bully bye bye\n- nerdy',
    'you make me cool (da da da da) ok i`m nerdy\n- nerdy',
    'not same (same), but trend (trend)\n- nerdy',
    'you can call me hopeless, but even if it looks boring, it catches \
    your eye\n- nerdy', 'who are you? i`m the queen of the nerds\n- nerdy',
    'my world is odd, call me a question mark (uh)\n- nerdy',
    'i`m a weirdo duck, who let the duck, who, who cares what you think?\n- nerdy',
    'i`m only into what i like, i don`t mind \
    playing alone (n e r d! la-la-la-la-la)\n- nerdy',
    '(da da da da) bully bully, kick and bass\n- nerdy',
    'click click, all about me, all-all about me\n- nerdy',
    'kick-kick, dance with me (la-la-la-la-la)\n- nerdy'
]
fireflower = [
    'brightly burning alone, i don`t know where it`ll go\n- fireflower',
    'an unpredictable temperature, like a fire, like a flower\n- fireflower',
    'it`s not flashy, even if it blooms all the time, it`s not enough\n- fireflower',
    'oh, i-i-i, i-i, tell me what you think i am\n- fireflower',
    'yeah, i`m probably more red than that, the rose that is dyed \
    red, flame scarlet\n- fireflower',
    'oh, come on, feel it, rather than red light i`m...\n- fireflower',
    'become a blue flame, shine on this night\n- fireflower',
    'shoot it up, fire (fire) burn up, burn up\n- fireflower',
    'i will become a flower, spreading the fragrance so that i won`t \
    forget and lose\n- fireflower', 'bloom, la-la-la-la-la\n- fireflower',
    'rise up, la-la-la-la-la\n- fireflower',
    'the thorn that stabs painfully and traps me, burning beautifully \
    over and over again\n- fireflower',
    'this is my zone, i`m done with the ugly things\n- fireflower',
    'yes, i`m going crazy when i am breathing hot air\n- fireflower',
    'the black shadow is lifted, the place i passed by is nice\n- fireflower',
    'oh, i-i-i, i-i, will you leave me like this\n- fireflower',
    'the deeper i go, the hotter i get\n- fireflower',
    'more freely, like that blue sky, it`s burning inside me\n- fireflower',
    'so that the red flower does not wither, i`ll surround you \
    with fire and flowers\n- fireflower'
]
cantstopdreamin = [
    'a feeling that i cannot express in words, the \
    feeling that perfect days will unfold, you`ll find out soon\n- can`t stop dreamin`',
    'you will like it\n- cant stop dreamin`',
    'it bloomed silently, and i felt it for the first time\n- can`t stop dreamin`',
    'i don`t know what to do with this trembling \
    feeling, i got it\n- can`t stop dreamin`',
    'it`s as natural as dancing, i`ve always wanted\n- can`t stop dreamin`',
    'it`s like a dream, this moment right now\n- can`t stop dreamin`',
    'fly to the purple lit world\n- can`t stop dreamin`',
    'can`t stop dreamin` (dreamin`) can you imagine?\n- can`t stop dreamin`',
    'say yeah, yeah, yeah, yeah\n- can`t stop dreamin`',
    'in the quiet darkness, i am a bright light\n- can`t stop dreamin`',
    'the gravity that pulls me here\n- can`t stop dreamin`',
    'fly-y-y to me, looking, my eye-eye-eyes\n- can`t stop dreamin`',
    'i`ll fall deep into this moment\n- can`t stop dreamin`',
    'we become free as if time has stopped\n- can`t stop dreamin`',
    'don`t wait, just go, just tell me where i got to go\n- can`t stop dreamin`',
    'go all the night, don`t get tired, i`ll hug you\n- can`t stop dreamin`',
    'dye it the same color as me\n- can`t stop dreamin`',
    'my future that will be completed, the picture i \
    dreamed of since a long time ago\n- can`t stop dreamin`',
    'when the pictures match one by one, we will be \
    shining forever\n- can`t stop dreamin`',
    'now is the time, that will make your heart beat\n- can`t stop dreamin`',
    'yes, if you and i are together, our dream becomes clearer\n- can`t stop dreamin`'
]
loveisdead = [
    'bad, you`re like a ghost, disappearing every day\n- love is dead',
    'say the same lie, love again (no,no,no,uh-uh,uh)\n- love is dead',
    'happy endings, everything, it all turns into a nightmare\n- love is dead',
    'everything is messed up, everything, everything, everything\n- love is dead',
    'you give me something, baby, it makes me scared, baby\n- love is dead',
    'this feeling`s bad, i hate it so much, my love is already broke\n- love is dead',
    '(ooh-woah) you broke it, i don`t want to know\n- love is dead',
    '(ooh-woah) ain`t got nothing, it`s all stolen\n- love is dead',
    '(ooh-woah) i don`t believe you, either way it`s all (bad)\n- love is dead',
    'you know what? love, love, love is dead\n- love is dead',
    'you know what? love, love, love is bad\n- love is dead',
    'it`s all over my body, digging firmly in my head\n- love is dead',
    'bang, bang, bang, bang, bang, my love is dead\n- love is dead',
    'da, da, da, da-da-da, da, da (oh, woah, woah) \n- love is dead',
    'uh, my love is already dead, but what can i do? i`m not sad\n- love is dead',
    'let`s party, open a champagne, cheers to our farewell\n- love is dead',
    'ayy, ayy you can`t hold onto my feet\n- love is dead',
    'my mind`ll never change anyway\n- love is dead',
    '(ooh-woah) you took it, only bad things\n- love is dead',
    '(ooh-woah) you made me be nice\n- love is dead',
    'love is dead, i`m not cool anymore\n- love is dead',
    'love is dead, i can`t feel anything\n- love is dead',
    'clearly on my body, i hate you, you cut deeply on my skin\n- love is dead'
]
summerrain = [
    'summer rain drop, drop, dropping like my sigh\n- SuMMer RaiN',
    '24/7 love is a never-ending lie\n- SuMMer RaiN',
    'after the rain falls, i feel high, high, and low, oh\n- SuMMer RaiN',
    'tangled inside my cloudy memories, doubt in my head now, oh\n- SuMMer RaiN',
    'why did you cover up the light?\n- SuMMer RaiN',
    'no matter how hard i try, no way\n- SuMMer RaiN',
    'worry `bout a thing, left alone with my useless regrets, uh-oh\n- SuMMer RaiN',
    'when you faded away, i was so disappointed\n- SuMMer RaiN',
    'let me paint again, a pain too deep\n- SuMMer RaiN',
    'are you happier, happier, happier now?\n- SuMMer RaiN',
    'today i stand here again\n- SuMMer RaiN',
    'our story ends here, say you wanna stay here, never say goodbye\n- SuMMer RaiN',
    'say you wanna love me, never say goodbye\n- SuMMer RaiN',
    'summer rain, 24/7 love, tears never stop\n- SuMMer RaiN',
    'yeah, humid air, colorful faces filled the street i used \
    to walk with you\n- SuMMer RaiN',
    'we are now at the end of a slanted roof,, it`s broken, \
    that`s all, too tough to endure\n- SuMMer RaiN',
    'i`ma fake it, i`ma leave\n- SuMMer RaiN',
    'wanna fake it, set me free (oh)\n- SuMMer RaiN',
    'only the tears fall under the umbrella we used to share (oh)\n- SuMMer RaiN',
    'i`ll let you go now, love is a broken chain (oh)\n- SuMMer RaiN',
    'i will let you go like the falling rain (oh)\n- SuMMer RaiN',
    'summer rain drop, drop, dropping like my sigh \
    (summer rain dries in my eye)\n- SuMMer RaiN'
]
geekyland_lyrics = random.choice([byebyebully, nerdy, fireflower,
                                 cantstopdreamin, loveisdead, summerrain])
# cabin fever lyrics 5th ep
introsaveme = [
    'bite me, deeper, crazier than ever, every single moment\n- intro:save me',
    'party is over, who is the savior? drippin` drippin` purple juice\n- intro:save me',
    'i came to bring the pain, this is not insane\n- intro:save me',
    'straight out of hell, i don`t make it back\n- intro:save me',
    'drippin` drippin` purple juice\n- intro:save me',
    'save me, save me, still you want me\n- intro:save me',
    'next to me, next to me, when you save me\n- intro:save me',
    'da la la la la, da la la la la save me, save me\n- intro:save me'
]
sweetjuice = [
    'light this candle that will wake the darkness, find yourself unable to bear it?\
     so do i\n- sweet juice',
    'we`ve starvin` for so long, i`m out of control\n- sweet juice',
    'it`s time to wake the sleeping madness in me\n- sweet juice',
    'ah, i need some fresh air now, come closer, i`ll whisper to you\n- sweet juice',
    'you want some sweet juice? chew it, pop it, pop it\n- sweet juice',
    'slowly drippin` drippin` follow the instinct\n- sweet juice',
    'heaven, this taste is sweety, sweety\n- sweet juice',
    'nerves all over the body, dance, ta-ra-ta-ra\n- sweet juice',
    'no time to think about this and that, like a flame, it all burns,\
     it all gets on\n- sweet juice',
    'nothing can lock us up, it all gets on this wind\n- sweet juice',
    'i want some sweet juice\n- sweet juice',
    'mm, you want it too, this sweet juice\n- sweet juice',
    'this throat-burning sensation is taboo\n- sweet juice',
    'my brain rule it like tattoo, yeah, yeah\n- sweet juice',
    'i feel so good, this taste might hook me up\n- sweet juice',
    'hold your breath, keep it quiet, lay down, the footsteps are \
    silence, shh, nobody knows\n- sweet juice',
    'ah, i need some fresh air now, come closer, i`ll take you with me\n- sweet juice',
    'love it, tasty, want it, so sweety\n- sweet juice',
    'end up unconsciously wanting and searching for it, again towards the \
    gap that shines from afar\n- sweet juice',
    'i want it more and more\n- sweet juice',
    '(sweet juice) now i`m thirsty, thirsty (worth the pleasure)\n- sweet juice',
    'out there runnin`, runnin` (runnin`) come and follow me\n- sweet juice',
    'have fun (you know i gotta have it)\n- sweet juice',
    'soon the party starts (oh-oh) at times like this, slowly (oh-oh)\
     come and follow me\n- sweet juice',
    'we through, yeah-yeah, such a dream moment\n- sweet juice',
    'sweet juice, follow, oh, to our hearts` content\n- sweet juice'
]
t4ke = [
    'i don`t need meaningless “right and wrong”\n- t4ke',
    'don`t share your useless things, babe\n- t4ke',
    'you are just a transitory fairytale, but you`re everywhere\n- t4ke',
    'you need me `till the end\n- t4ke',
    'i`m already where i want to be, you already know\n- t4ke',
    'left, right, wherever you are, take down\n- t4ke',
    'we wouldn`t ever fall out, and it makes you feel low, low\n- t4ke',
    'even if everything`s dark, we won`t stop anymore, don`t stop, \
    we gonna keep on\n- t4ke',
    'ah-ah-ah-ah, ooh, ah-ah-ah-ah, i would be the one, left, right, yeah\n- t4ke',
    'i would be the one\n- t4ke',
    'i would be the one to take you down, i would be the one to take\n- t4ke',
    'yeah, yeah, i would be the one to take\n- t4ke',
    'uh, i`m different from the world you see, born to be queen, \
    i`m at the top already\n- t4ke', 'ah, say, never be the same\n- t4ke',
    'you can`t ever ruin me, i`ll never be alone\n- t4ke',
    'i will brutally show you a bad dream, to me, it`s just a heavy, \
    sweet cream\n- t4ke',
    'you wanna try, come to me, wherever you are, i`ll show you a take-down\n- t4ke',
    'as i want, already, you can`t get away\n- t4ke',
    'i`m just running, keep running\n- t4ke',
    'meanwhile, i`m being made in the days, if we continue on \
    this path, we take all\n- t4ke',
    'i dance alone in the moonlight (oh) i dance alone in the moonlight\n- t4ke'
]
autopilot = [
    'autopilot, ooh-ooh-ooh, oh\n- autopilot',
    'tonight, i`m free to go as i want\n- autopilot',
    'far and wide, anywhere, across the obscure night\n- autopilot',
    'in a flash, i accelerate (if it`s for you, it`s okay) and move \
    as if attracted to the cold city\n- autopilot',
    'maybe you are like gravity, i`m running to you \
    unconsciously, automatically\n- autopilot',
    'i feel like a monster, nobody can stop\n- autopilot',
    'even if i get hurt fearlessly, i never change my mind, like \
    autopilot, autopilot\n- autopilot',
    'rock you like a hurricane, nothing can stop me\n- autopilot',
    'even if you push me, always on my mind, like autopilot, autopilot\n- autopilot',
    'run away with me as if it`s your last day\n- autopilot',
    'without anyone knowing (by your side) i`ll never let you go\n- autopilot',
    'the world i see with my half-closed eyes, it`s already full with \
    your existence\n- autopilot',
    'no turning back, i`ll just look forward and run (ooh-ooh-woah-oh)\n- autopilot',
    'yeah, i can`t stop my heart that`s drawn to you\n- autopilot',
    'ride a contrail, go straight only for you\n- autopilot',
    'right now, i leave everything to you, trust me\n- autopilot',
    'again and again, make my heart beat, you make me autopilot\n- autopilot'
]
agit = [
    'i dust off the old radio, so it looks like the day i bought it\n- agit',
    'my favorite song playing, something feels different, like that\n- agit',
    'i can feel those days` memories that had become blurry\n- agit',
    'baby, in here, feels like dreaming innocent, i started to hope \
    i`ll dream again\n- agit',
    'this connection is undeniable, there`s no doubt about that\n- agit',
    'our own hideout, my youth fantasy with you, i have nothing to fear\n- agit',
    'watch you, i look right at you step by step, dancing through life\n- agit',
    'roll, roll, just let it blow, you and i just roll\n- agit',
    'my heart is a sky full of fireworks\n- agit',
    'the first time`s excitement and the sad moments as well\n- agit',
    'the good morning came back, i still feel the spark, it`s still \
    shining brightly\n- agit',
    'baby, in here, feels like dreaming innocently\n- agit',
    'i feel like i`m dreaming again\n- agit',
    'hideout, if i`m with you, so fine\n- agit',
    'precious, if we`re like this, we`ll never feel tired\n- agit',
    'uh, uh, yeah, looks so good (woo)\n- agit',
    'if it`s just us, we never stop smiling (ah) every day is party mood\n- agit',
    'i`ll never forget the light or this moment (my youth fantasy)\n- agit',
    'i`ll never forget you and i holding hands\n- agit',
    'roll (so hot, baby) roll (so hot, baby) (just let it blow)\n- agit',
    'i`ll never get tired with you, baby (you and i just roll)\n- agit',
    'i just want you more\n- agit'
]
sofarsogood = [
    'can you see the distant yet close line?\n- so far so good',
    'the faintly sharp gap between us? If you show me even \
    half of your heart, it`s good to be around, yeah\n- so far so good',
    'i have special issues with you\n- so far so good',
    'i always wonder about you, even if i resist, i think about you \
    too much\n- so far so good',
    'so far, so good, no doubt about anything between us, it`s perfect \
    so far\n- so far so good',
    'i`m still afraid, i might be scared, but\n- so far so good',
    'what is we drink all night and talk until the sunrise?\n- so far so good',
    'because i wanna know you, you-u-u, you-u-u, so far so good, i want \
    you\n- so far so good',
    'du-du-du, du-du, du-du-du, ooh-ooh-ooh-woah\n- so far so good',
    'du-du-du, du-du, du-du-du, so far so good, i want you\n- so far so good',
    'look, i seem somehow unfamiliar, hiding my heartbeat anywhere\n- so far so good',
    'talk to me, yeah, my heart keeps beating crazy\n- so far so good',
    'i`m like a broken clock, yeah\n- so far so good',
    'no matter if i pretend not to, it`s obvious that i`m anxious\n- so far so good',
    'i still don`t know, even though you`re mine\n- so far so good',
    'somehow, it`s not easy, it might take a while\n- so far so good',
    'if countless nights pass, but i`m with you, it`s as good as it \
    gets, yeah\n- so far so good',
    'under the faint light, you shine more than anything\n- so far so good',
    'you make it too unbearable for me\n- so far so good',
    'don`t hesitate, give me more\n- so far so good',
    'don`t whisper, get closer, if you really really love me\n- so far so good'
]
cabfev_lyrics = random.choice([introsaveme, sweetjuice, t4ke, \
                               autopilot, agit, sofarsogood])

# swan solo 1st ep
twenty = [
    'there was once a little girl that i remember, won`t forget\n- twenty',
    'oh,\
that look of joy right on her face, one so young and just a child, and singing, dancing\
through the night\n- twenty',
    'you and i were feeling rather good, suddenly you`re\
grown up but it seems your wings are gone\n- twenty',
    'even though you`re afraid i`m \
feeling you, if you`re here with me, then\n- twenty',
    'let`s all dance any way you\
feel, any way you want, hold me close, fly away\n- twenty',
    'i love you, shining on me\
bright, you`re my only light\n- twenty',
    'i just wanna say, like a twinkling star, my\
twenty\n- twenty',
    'always on me, my own spotlight, like a time that never will come\
back, i love you\n- twenty',
    'when the light is dimming and if you`re scared of the\
dark, find that special someone who will shine on you\n- twenty',
    'so i, `cause i`m\
feeling you, if you are here with me\n- twenty',
    'life is falling fast asleep when\
everything is turning off (ooh)\n- twenty',
    'the darkness finding me, even though i`m\
afraid, open up the door and feel the shining light, let`s dance\n- twenty',
    'let`s all\
dance, been waiting for this time to come, just like me\n- twenty',
    'i`m gonna fly and\
spread my wings, no i cannot stop you (i love you)\n- twenty',
    'i love you, you are\
like my shining star when you light me up (i love you)\n- twenty',
    'real me gonna show\
what i`m like, dont care `bout them others\n- twenty',
    'moments stuck in my head, my\
twenty, on me, twenty-four-seven spotlight\n- twenty'
]
everything = [
    'whenever you look over here, it feels like we`re frozen in time\n- be my\
everything',
    'i was cold as ice but i`m melting now, butterflies they bloom in my heart\
\n- be my everything',
    'and every time you caress me, our moments will stay in my head\
\n- be my everything',
    'when i look around, over your way, feels like we are with each\
other now\n- be my everything', 'please be my everything\n- be my everything',
    'i alw\
ays had a dream, you`d be my own little world\n- be my everything',
    'you and me (you`re\
 my everything)\n- be my everything',
    'whenever you shine on me, you go and light me up\
\n- be my everything',
    'all the stars in the night sky, they dance along with us\n- be\
 my everything',
    'be my everything, this is love, i feel like i know\n- be my every\
thing', 'cannot stop it now, me heart is trembling, let me just feel with you\
\n- be my everything',
    'when i look around me, can`t get any closer, you`re in front\
 of me in the opposite direction\n- be my everything',
    'even accidentally, maybe you\
 could look here, you could find out just how i feel\n- be my everything',
    'i think i\
 know the situation, could someone lik you know someone like me?\n- be my every\
thing',
    'and the deeper that it gets, the more painful you are, and i hate myself\
 `cause i can`t stop it\n- be my everything',
    'no stopping this heart, can`t you\
 look at me? (be my everything)\n- be my everything'
]
twen_lyrics = random.choice([twenty, everything])

# festa lyrics 1st single ep
heaven = [
    '24/7 seven seven seven - heaven',
    'our own heaven heaven heaven heaven - heaven',
    'woo woo 24/7 (seven seven seven) let`s fill it with us - heaven',
    'i wanna fall deep into the world, reflecting on the moonlight on \
    that silver sand - heaven',
    'i feel like i`m gonna fly high high high - heaven',
    'under the starlight, we are dancing - heaven',
    'fly high, i wanna fly anywhere maybe i`ll just go away - heaven',
    'i wanna walk toward the galaxy far up there - heaven',
    'all the moments and day stay in front of me, they get me excited \
    that i can`t stop now - heaven',
    'you are my fantastic magic, my heart`s pounding so hard all day - heaven',
    'it`s time to party likey, let`s begin our special festival now, baby - heaven',
    'divin` to the galaxy with you, let’s fill it with us - heaven',
    'i wanna jump in freely, beb, i wanna fall for you, boogie on and on - heaven',
    'i can never have enough, i want more more - heaven',
    'all day yea, let`s fire it up and celebrate - heaven',
    'countless stars are shining, the purple sky is spreading - heaven',
    'it`s a festival for all, everybody, get ready now - heaven',
    'the stars shining up in the sky, they`re shining upon \
    us even brighter as if this is our last moment, it`s time \
    to celebrate 24/7 - heaven'
]
biscuit = [
    'i feel like i`ve discovered all your love, it seems like it won`t \
    ever leave - biscuit',
    'whatever one may do, would you mind if i let it flow without thinking - biscuit',
    'no matter what you say, it`s okay, im naturally like this - biscuit',
    'i don’t like this, like i’m trying to be good for others - biscuit',
    'decorating myself with a beautiful exterior, i live as i please (yeah) - biscuit',
    'biscuit, sometimes like this - biscuit',
    'i`m so wet, relaxing in the rain, on my way, it`s okay. oh, why? - biscuit',
    'don`t pay attention to me, i`m fed up with this - biscuit',
    'it`s unnecessary attention, i don`t accept that - biscuit',
    'don`t worry it`s just how i am, even if my heart thumps and \
    falls slowly up and down - biscuit',
    'i`ll just dive into this life, there`s no need to hide - biscuit',
    'it`s okay even if i`m a little scared - biscuit',
    'in the moment i realized it, everything seems beautiful - biscuit',
    'even if i can`t turn back, even if it becomes pitch dark, \
    it`s okay, i have myself - biscuit',
    'don`t be afraid, it`s the only way forward - biscuit',
    'may your shining eyes never disappear - biscuit'
]
mistake = [
    'there must be something underwater, and i know the truth - mistake',
    'i call you again, shattered, you`re the one with no answers - mistake',
    'i know you can just love me tonight, i`ve forcibly \
    swallowed those words - mistake',
    'if you tell me lies, i don`t want to know, i could pretend, \
    why do you keep spitting out cold words so easily? - mistake',
    'you were foolish, it was a mistake, tell me that i`m not your mistake - mistake',
    'i feel it like you do - mistake',
    'you`ve washed away everything from your heart,no matter how \
    many times i try to comb through, my night remains tangled - mistake',
    'the mistake from back then that can`t be corrected (oh-oh) - mistake',
    'kick step, the trust that had crumbled, you left as if you were \
    expecting the end - mistake',
    'we could be there, love will die - mistake',
    'you could be my love, but you`re gonna fade away - mistake',
    'the gap between us is growing wider, i`m escaping from the dream - mistake',
    'it`ll be the same, a little bitter, but it`s a shame, forget it - mistake',
    'your words that came to mind for no reason, ooh hoo - mistake',
    'ooh-ooh, ooh mistake all the time, you`re my mistake all the time, yeah - mistake',
    'ooh-ooh, ooh mistake all the time, i`m your mistake all the time - mistake',
    'i don`t want our love too easily - mistake',
    'piercing me deep with the same reasons again, it was \
    mistake that seemed like nothing - mistake',
    'coloring the dead memories of both of us that had withered - mistake',
    'back then, filled with harsh words, our emotions were white (ooh-ooh) - mistake',
    'we never let go of each other`s hands, you left as if you \
    were expecting the end(wake up) - mistake',
    'i`m living just fine without you, my heart is slowly scattering - mistake',
    'it seems like it`s over, for no reason again, someday i`ll \
    forget you, who had no meaning, oh, woah-oh - mistake'
]
fest_lyrics = random.choice([heaven, biscuit, mistake])

all_lyrics = twen_lyrics + cabfev_lyrics + fest_lyrics + intoviolet_lyrics + hideseek_lyrics + mymy_lyrics + memem_lyrics + geekyland_lyrics

