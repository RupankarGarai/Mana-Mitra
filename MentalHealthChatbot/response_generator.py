import random

def dynamic_response(user_message):
    """ Generate a dynamic response if no match is found. """
    if "study" in user_message:
        return random.choice([
            "It sounds like you're focused on studying. Try setting specific study goals to stay motivated.",
            "Everyone studies differently. Find what works best for you, whether it’s early mornings or late evenings.",
            "Don’t forget to take short breaks during study sessions to keep your mind fresh!"
        ])
    elif "stress" in user_message:
        return random.choice([
            "Managing stress is important. Try deep breathing exercises or taking a short walk to clear your mind.",
            "If you're feeling stressed, talk to someone or try writing your thoughts in a journal.",
            "Make sure you're getting enough rest and downtime to manage stress effectively."
        ])
    elif "motivation" in user_message:
        return random.choice([
            "Motivation can fluctuate. Keep your long-term goals in mind and celebrate small wins.",
            "Set small, achievable goals and reward yourself when you complete them to stay motivated.",
            "Sometimes a change of environment can boost your motivation. Try studying in a new spot!"
        ])
    elif "anxiety" in user_message:
        return random.choice([
            "Anxiety can be tough. Try grounding techniques like focusing on your breathing or counting objects around you.",
            "If you're feeling anxious, consider talking to someone you trust or practicing mindfulness.",
            "Remember, anxiety is natural, and taking a moment to pause and reflect can help."
        ])
    elif "time management" in user_message:
        return random.choice([
            "Effective time management is key to success. Try breaking tasks into smaller, manageable chunks.",
            "Consider using a schedule or a to-do list to better manage your time and reduce overwhelm.",
            "Set priorities for your tasks and tackle the most important ones first."
        ])
    elif "procrastination" in user_message:
        return random.choice([
            "Procrastination happens to everyone. Try setting small, easy tasks to get started and build momentum.",
            "Break larger tasks into smaller steps to avoid feeling overwhelmed and reduce procrastination.",
            "Set short deadlines and reward yourself for completing tasks to overcome procrastination."
        ])
    elif "sleep" in user_message:
        return random.choice([
            "Good sleep is essential for mental health. Try to maintain a consistent sleep schedule to improve your rest.",
            "A bedtime routine, like reading or practicing relaxation techniques, can help you sleep better.",
            "If you're struggling with sleep, try avoiding screens before bed and create a calming sleep environment."
        ])
    elif "social life" in user_message:
        return random.choice([
            "Balancing social life and academics can be challenging. Try to make time for friends while also setting study goals.",
            "It's okay to say no sometimes. Prioritize what's most important for your well-being.",
            "Engage in activities that you enjoy, and don’t be afraid to take breaks to spend time with friends."
        ])
    elif "focus" in user_message:
        return random.choice([
            "If you're struggling to focus, try the Pomodoro technique: work for 25 minutes, then take a short break.",
            "Reducing distractions, like putting away your phone, can help you stay focused.",
            "Focus on one task at a time to avoid multitasking, which can reduce your overall productivity."
        ])
    elif "exercise" in user_message:
        return random.choice([
            "Exercise is a great way to boost mental health. Even a short walk can clear your mind and improve mood.",
            "Incorporating regular physical activity into your routine can improve both focus and energy levels.",
            "Try different forms of exercise, such as yoga or dancing, to find what you enjoy the most."
        ])
    elif "diet" in user_message:
        return random.choice([
            "Maintaining a balanced diet can have a significant impact on your energy and mental clarity.",
            "Don’t skip meals, especially during stressful times. Keep healthy snacks available to stay nourished.",
            "Staying hydrated and eating nutrient-rich foods can help improve your focus and mood."
        ])
    elif "relationships" in user_message:
        return random.choice([
            "Healthy relationships are built on trust and communication. Make time to check in with loved ones.",
            "It’s important to set boundaries in relationships to maintain a sense of balance and personal space.",
            "Conflict in relationships is natural. Approach it with an open mind and try to listen actively."
        ])
    elif "self-esteem" in user_message:
        return random.choice([
            "Building self-esteem takes time. Start by acknowledging your strengths and accomplishments.",
            "Surround yourself with positive people who support and uplift you.",
            "Practice self-compassion. Speak to yourself as you would to a close friend when you make mistakes."
        ])
    elif "depression" in user_message:
        return random.choice([
            "If you're feeling down, consider reaching out to someone you trust or a professional for support.",
            "It's okay to not feel okay sometimes. Take small steps to care for yourself, like getting some fresh air.",
            "Remember that you're not alone, and help is available. Talking about how you feel can be a big first step."
        ])
    elif "mindfulness" in user_message:
        return random.choice([
            "Mindfulness can help calm the mind. Try focusing on your breathing for a few minutes to relax.",
            "Taking a few minutes a day to practice mindfulness, like observing your surroundings, can reduce stress.",
            "Mindfulness exercises can improve concentration and help you feel more grounded during busy times."
        ])

    elif "loneliness" in user_message:
        return random.choice([
            "Loneliness can be tough, but connecting with others, even online, can help you feel less isolated.",
            "Try joining a club or group where you can meet people with similar interests to reduce loneliness.",
            "Remember, it's okay to feel lonely sometimes. Reaching out to friends or family can make a big difference."
        ])
    elif "bullying" in user_message:
        return random.choice([
            "Bullying is serious. Don’t hesitate to talk to someone you trust, like a teacher or counselor.",
            "If you're being bullied, remember it's not your fault, and there are people who can help.",
            "Stay strong and seek support. No one deserves to be treated poorly or bullied."
        ])
    elif "confidence" in user_message:
        return random.choice([
            "Building confidence takes time. Start with small challenges, and celebrate your achievements.",
            "Practice positive self-talk. Remind yourself of the things you're good at.",
            "Confidence grows when you step outside your comfort zone, even just a little bit."
        ])
    elif "peer pressure" in user_message:
        return random.choice([
            "Peer pressure can be difficult. Stay true to your values and don’t be afraid to say no.",
            "Surround yourself with friends who respect your choices and support your decisions.",
            "Remember, you don’t have to do something just because everyone else is. Make decisions that feel right for you."
        ])
    elif "failure" in user_message:
        return random.choice([
            "Failure is part of growth. Learn from it, but don’t let it define you.",
            "Everyone fails at some point. What matters is how you pick yourself back up.",
            "Failure is an opportunity to try again with more knowledge and experience."
        ])
    elif "exams" in user_message:
        return random.choice([
            "Exams can be stressful, but breaking your revision into smaller chunks can help.",
            "Try to focus on one subject at a time during exam preparation to avoid feeling overwhelmed.",
            "Remember to take care of yourself during exam season—sleep and nutrition are just as important as studying."
        ])
    elif "friends" in user_message:
        return random.choice([
            "Good friends are an important support system. Don’t hesitate to reach out to them when you need to talk.",
            "Friendships require effort from both sides. Be open and honest with your friends about how you feel.",
            "It’s okay if friendships change over time. Focus on those who lift you up and support you."
        ])
    elif "perfectionism" in user_message:
        return random.choice([
            "Perfectionism can be overwhelming. Remember, it's okay to make mistakes and learn from them.",
            "No one is perfect. Aim for progress, not perfection, and be kind to yourself along the way.",
            "Perfectionism can lead to burnout. Set realistic goals and remember to take breaks."
        ])
    elif "distraction" in user_message:
        return random.choice([
            "If distractions are an issue, try limiting your environment to the essentials for focus.",
            "Using techniques like the Pomodoro method can help reduce distractions and improve focus.",
            "Identify what’s distracting you and create a plan to minimize it during your study or work time."
        ])
    elif "overwhelm" in user_message:
        return random.choice([
            "Feeling overwhelmed? Break tasks into smaller steps and tackle them one at a time.",
            "It’s okay to ask for help when things feel overwhelming. Don’t be afraid to lean on others.",
            "Take deep breaths and focus on what you can control when you feel overwhelmed."
        ])
    elif "anxiety" in user_message:
        return random.choice([
            "Anxiety is normal, but it’s important to manage it. Deep breathing exercises can help calm your nerves.",
            "If you're feeling anxious, try writing down your thoughts or talking to someone you trust.",
            "When anxiety strikes, focus on grounding techniques like noticing things around you or practicing mindfulness."
        ])
    elif "sleep" in user_message:
        return random.choice([
            "Getting enough sleep is crucial. Try setting a consistent bedtime routine to improve your sleep quality.",
            "Avoid using screens before bed to help your brain wind down for better sleep.",
            "If you're struggling to sleep, relaxation exercises like deep breathing or meditation can help."
        ])
    elif "time management" in user_message:
        return random.choice([
            "Effective time management involves prioritizing tasks. Start with the most important and break it into steps.",
            "Try using a to-do list or planner to organize your tasks and manage time more efficiently.",
            "Time management is a skill. Practice balancing your workload with short breaks to stay productive."
        ])
    elif "procrastination" in user_message:
        return random.choice([
            "Procrastination happens to everyone. Try breaking tasks into smaller parts to make them less daunting.",
            "Set short, achievable goals to stay focused and beat procrastination.",
            "Sometimes just getting started is the hardest part. Set a timer for 5 minutes and begin—you might find it easier to keep going."
        ])
    elif "social media" in user_message:
        return random.choice([
            "Social media can be a big distraction. Try setting limits on your usage to stay focused.",
            "Remember, what you see on social media is often a highlight reel. Don’t compare yourself to others.",
            "Taking breaks from social media can improve your mental health and reduce stress."
        ])
    elif "self-care" in user_message:
        return random.choice([
            "Self-care is important. Take time for activities that make you feel good, whether it’s reading, exercise, or a hobby.",
            "Make self-care a priority in your routine—it helps maintain mental and physical well-being.",
            "Remember that self-care isn’t selfish. Taking care of yourself allows you to better support others."
        ])
    elif "relationships" in user_message:
        return random.choice([
            "Healthy relationships are built on trust and communication. Don’t hesitate to talk openly about how you feel.",
            "It’s okay to set boundaries in relationships. Respect yourself and others will follow suit.",
            "Every relationship has ups and downs. Focus on understanding and supporting each other during tough times."
        ])
    elif "focus" in user_message:
        return random.choice([
            "To improve focus, minimize distractions around you and take regular breaks to refresh your mind.",
            "Sometimes changing your environment can boost your focus, whether it's a new study spot or background noise.",
            "Focus comes with practice. Start with shorter tasks and gradually build your concentration."
        ])
    elif "mindfulness" in user_message:
        return random.choice([
            "Practicing mindfulness can help reduce stress. Try focusing on the present moment without judgment.",
            "Mindfulness can be as simple as noticing your breath or tuning into your senses.",
            "Incorporating mindfulness into your daily routine can improve your mental clarity and emotional well-being."
        ])
    elif "mental health" in user_message:
        return random.choice([
            "Mental health is just as important as physical health. Make time to check in with yourself and how you’re feeling.",
            "It’s okay to not be okay. Reach out to a friend, family member, or counselor if you’re struggling with your mental health.",
            "Taking care of your mental health could involve practicing relaxation techniques, physical activity, or talking to someone."
        ])
    elif "productivity" in user_message:
        return random.choice([
            "To boost productivity, try breaking down larger tasks into manageable steps and tackling them one by one.",
            "Productivity increases with proper rest. Don’t forget to take short breaks to avoid burnout.",
            "Stay organized by keeping a list of tasks and prioritizing them based on importance or deadlines."
        ])
    elif "burnout" in user_message:
        return random.choice([
            "Burnout is a sign that you need rest. Try to take time off to recharge mentally and physically.",
            "It’s important to recognize the signs of burnout—tiredness, irritability, and lack of motivation. Take care of yourself.",
            "If you’re feeling burned out, prioritize self-care and ask for help if your workload is overwhelming."
        ])
    elif "self-esteem" in user_message:
        return random.choice([
            "Building self-esteem takes time. Focus on your strengths and what makes you unique.",
            "Positive affirmations can help improve your self-esteem. Remind yourself of your worth daily.",
            "Self-esteem grows when you step outside your comfort zone. Celebrate your courage and progress."
        ])
    elif "goal setting" in user_message:
        return random.choice([
            "Setting realistic and specific goals can help you stay motivated and focused on what you want to achieve.",
            "Break down big goals into smaller, manageable tasks to avoid feeling overwhelmed.",
            "Track your progress regularly to stay on course and adjust your goals as needed."
        ])
    elif "failure" in user_message:
        return random.choice([
            "Failure is part of learning. Don’t let it define you—focus on what you can learn from it.",
            "Everyone experiences failure at some point. It’s how you bounce back that matters most.",
            "Failure is an opportunity to grow. Reflect on what went wrong and use it to improve next time."
        ])
    elif "perfectionism" in user_message:
        return random.choice([
            "Perfectionism can hold you back. Remember, done is better than perfect!",
            "It's okay to make mistakes. Perfectionism can be exhausting, so give yourself some grace.",
            "Perfectionism can limit creativity. Focus on progress, not perfection."
        ])
    elif "friendship" in user_message:
        return random.choice([
            "Good friendships are based on trust and respect. Don’t be afraid to open up to your friends.",
            "Friendship takes effort from both sides. Make sure to communicate openly and honestly.",
            "Cherish your friends, but remember it’s okay to set boundaries if you need personal space."
        ])
    elif "loneliness" in user_message:
        return random.choice([
            "Feeling lonely is tough, but you're never truly alone. Reach out to friends or join a new group to meet people.",
            "It's normal to feel lonely sometimes. Talking to someone about it can make a big difference.",
            "Loneliness can be overwhelming, but connecting with others, even in small ways, can help."
        ])
    elif "depression" in user_message:
        return random.choice([
            "If you're feeling depressed, it's important to talk to someone, whether it’s a friend, family member, or counselor.",
            "Depression can make things feel hopeless, but remember that you're not alone—help is available.",
            "It’s okay to not feel okay. Don’t hesitate to seek professional help if you're feeling depressed."
        ])
    elif "focus on studies" in user_message:
        return random.choice([
            "To improve focus on studies, try using techniques like Pomodoro—study for 25 minutes, then take a 5-minute break.",
            "If you’re struggling to focus, remove distractions like your phone and create a designated study space.",
            "Sometimes switching up study environments or routines can help refresh your focus."
        ])
    elif "overthinking" in user_message:
        return random.choice([
            "Overthinking can be exhausting. Try to redirect your thoughts by focusing on the present moment.",
            "If you find yourself overthinking, journaling can help you organize your thoughts and let go of unnecessary worries.",
            "Overthinking won’t change the past or predict the future. Focus on what you can control right now."
        ])
    elif "peer pressure" in user_message:
        return random.choice([
            "Peer pressure can be tough, but staying true to yourself is more important than fitting in.",
            "It’s okay to say no if something doesn’t feel right to you, even if your peers are doing it.",
            "Trust your instincts when dealing with peer pressure. Your values are more important than others’ expectations."
        ])
    elif "self-doubt" in user_message:
        return random.choice([
            "Self-doubt is natural, but remember to trust yourself and your abilities. You've made it this far!",
            "Whenever you experience self-doubt, remind yourself of past achievements and strengths.",
            "Overcoming self-doubt takes time. Be kind to yourself and focus on progress rather than perfection."
        ])
    elif "study techniques" in user_message:
        return random.choice([
            "Everyone learns differently. Experiment with different study techniques like mind maps, summaries, or flashcards.",
            "Active learning techniques like self-quizzing and teaching others can help reinforce your knowledge.",
            "Break up study sessions with short breaks to retain information better and stay energized."
        ])
    elif "test anxiety" in user_message:
        return random.choice([
            "Test anxiety is common, but preparation can help. Practice deep breathing to calm nerves before a test.",
            "Try to focus on your preparation rather than the outcome to ease test anxiety.",
            "Test anxiety can be reduced by creating a study plan and practicing relaxation techniques before the exam."
        ])
    elif "perseverance" in user_message:
        return random.choice([
            "Perseverance is key to achieving your goals. Keep pushing through challenges and trust the process.",
            "Success often comes from perseverance, not just talent. Keep going, even when things get tough.",
            "Remember that setbacks are temporary. With perseverance, you can overcome obstacles and succeed."
        ])
    elif "empathy" in user_message:
        return random.choice([
            "Empathy is about putting yourself in others’ shoes. It helps build stronger, more meaningful relationships.",
            "Practicing empathy can improve communication and understanding in friendships and family relationships.",
            "Empathy involves listening without judgment. Give people the space to share their feelings."
        ])
    elif "discipline" in user_message:
        return random.choice([
            "Discipline is about consistency. Focus on creating small daily habits that add up over time.",
            "Self-discipline can be challenging, but breaking tasks into smaller steps can make it easier to stay on track.",
            "Discipline is key to reaching your goals. Stay focused and reward yourself for sticking to your routine."
        ])
    elif "gratitude" in user_message:
        return random.choice([
            "Practicing gratitude can improve your mood and mental well-being. Try writing down a few things you're thankful for each day.",
            "Gratitude helps shift your focus from what's lacking to what you already have.",
            "Showing gratitude to others can strengthen relationships and create a positive mindset."
        ])
    elif "happiness" in user_message:
        return random.choice([
            "Happiness can come from small, everyday moments. Focus on the present and enjoy life's little joys.",
            "Happiness isn’t about perfection. It's about appreciating what you have and where you are right now.",
            "Pursuing happiness involves finding balance—between work, rest, relationships, and self-care."
        ])
    elif "exercise" in user_message:
        return random.choice([
            "Regular exercise can boost your mood and energy levels. Try adding it to your daily routine.",
            "Exercise is a great way to manage stress and improve your mental well-being.",
            "Even a short walk or stretching session can lift your spirits and increase focus during study breaks."
        ])
    elif "nutrition" in user_message:
        return random.choice([
            "Good nutrition fuels your body and mind. Aim for a balanced diet with plenty of fruits and vegetables.",
            "Staying hydrated and eating nutritious meals can help you stay focused and energized.",
            "Healthy eating habits can improve both physical health and mental clarity, especially during stressful times."
        ])
    elif "time management" in user_message:
        return random.choice([
            "Time management is key to balancing studies and relaxation. Try using a planner to track tasks and deadlines.",
            "Break tasks into smaller chunks to manage your time more effectively and avoid feeling overwhelmed.",
            "Prioritize important tasks and avoid multitasking to improve time management."
        ])
    elif "procrastination" in user_message:
        return random.choice([
            "Procrastination happens to everyone. Set small, achievable goals to get started and build momentum.",
            "Sometimes it helps to break a large task into smaller steps to overcome procrastination.",
            "If you're procrastinating, try starting with just 5 minutes of focused work. Often, that's enough to keep going."
        ])
    elif "burnout" in user_message:
        return random.choice([
            "Burnout is a sign you need to take a break. Try stepping away from work to relax and recharge.",
            "If you’re feeling burnt out, focus on self-care—sleep, healthy eating, and doing something you enjoy.",
            "To avoid burnout, make sure you're balancing work with rest and fun activities."
        ])
    elif "self-care" in user_message:
        return random.choice([
            "Self-care is essential for mental health. Take time for yourself, whether it’s reading, exercising, or meditating.",
            "Remember that self-care isn't selfish; it helps you recharge and be more effective in other areas of your life.",
            "Daily self-care practices, like a morning walk or journaling, can help reduce stress and improve well-being."
        ])
    elif "sleep" in user_message:
        return random.choice([
            "A good night’s sleep is crucial for mental clarity. Try to keep a regular sleep schedule for better rest.",
            "If you're having trouble sleeping, create a bedtime routine that helps you wind down.",
            "Sleep impacts everything from mood to focus, so prioritize getting enough rest, especially before exams."
        ])
    elif "social anxiety" in user_message:
        return random.choice([
            "Social anxiety can be challenging, but practicing self-compassion and taking small social steps can help.",
            "If social anxiety is overwhelming, try relaxation techniques like deep breathing before social interactions.",
            "Focus on connecting with one person at a time to ease feelings of social anxiety."
        ])
    elif "comparison" in user_message:
        return random.choice([
            "It’s easy to compare yourself to others, but remember everyone’s journey is unique. Focus on your own progress.",
            "Comparing yourself to others can steal your joy. Celebrate your own strengths and achievements.",
            "Instead of comparing, try to use others’ success as motivation to improve and grow."
        ])
    elif "failure to meet expectations" in user_message:
        return random.choice([
            "It's okay if things don’t go as planned. Use setbacks as learning opportunities to grow stronger.",
            "Missing expectations can feel disappointing, but remember that progress isn't always linear.",
            "If you didn’t meet your expectations, reflect on what you can change and keep moving forward."
        ])
    elif "public speaking" in user_message:
        return random.choice([
            "Public speaking can be nerve-wracking, but practice can build confidence. Start with small audiences.",
            "Before speaking, take a few deep breaths to calm your nerves and focus on delivering your message.",
            "Prepare well and focus on the content, not just the audience, to ease public speaking anxiety."
        ])
    elif "goal setting" in user_message:
        return random.choice([
            "Setting realistic goals can keep you motivated. Break big goals into smaller, manageable tasks.",
            "Write down your goals and create a plan to achieve them, step by step.",
            "Goal setting is a powerful tool. Stay flexible and adjust your goals as you progress."
        ])
    elif "perfectionism in studies" in user_message:
        return random.choice([
            "Perfectionism in studies can create stress. Focus on effort and learning rather than perfect results.",
            "It's important to accept that no one gets everything right all the time. Progress is more important than perfection.",
            "Perfectionism can slow you down. Set realistic expectations for your studies and celebrate small achievements."
        ])
    elif "focus during exams" in user_message:
        return random.choice([
            "During exams, take regular breaks to keep your mind sharp and avoid burnout.",
            "Stay organized and manage your time wisely during exams to reduce stress.",
            "Before exams, try relaxation techniques like deep breathing to help you focus and stay calm."
        ])
    elif "building confidence" in user_message:
        return random.choice([
            "Confidence comes with practice. Start small, take risks, and learn from your experiences.",
            "Building confidence is about trusting yourself. Celebrate your successes, even the small ones.",
            "Confidence grows over time. Be patient with yourself and focus on gradual progress."
        ])
    elif "handling criticism" in user_message:
        return random.choice([
            "Receiving criticism can be hard, but it's an opportunity to learn and grow.",
            "Try not to take criticism personally. Instead, use it to improve your skills or approach.",
            "Constructive criticism can help you improve, but remember that not all feedback is accurate or helpful."
        ])
    elif "emotional intelligence" in user_message:
        return random.choice([
            "Emotional intelligence is about understanding your emotions and those of others. Practice empathy and self-awareness.",
            "Improving emotional intelligence can help with relationships and self-care. Reflect on your emotions regularly.",
            "Emotional intelligence grows with experience. Stay open to learning from both positive and difficult emotions."
        ])
    elif "mindfulness" in user_message:
        return random.choice([
            "Mindfulness is about staying present. Take a few moments each day to breathe and focus on the now.",
            "Practicing mindfulness can reduce stress and improve focus. Try it during study breaks or before bed.",
            "Mindfulness helps you manage emotions by acknowledging them without judgment. It’s a powerful tool for mental health."
        ])
    elif "creativity block" in user_message:
        return random.choice([
            "Creativity blocks happen to everyone. Step away for a bit and come back with fresh eyes.",
            "When experiencing a creative block, try doing something different to spark new ideas.",
            "Sometimes the best way to overcome a creative block is to let your mind rest and recharge."
        ])
    elif "financial stress" in user_message:
        return random.choice([
            "Financial stress is tough. Try creating a budget to manage your expenses and prioritize saving.",
            "Talk to someone about your financial concerns, whether it's a mentor or financial advisor. You don't have to go through it alone.",
            "It's okay to feel stressed about money, but make a plan to manage it step by step. Small changes can lead to big relief."
        ])
    elif "self-esteem" in user_message:
        return random.choice([
            "Building self-esteem takes time. Focus on your strengths and what makes you unique.",
            "Self-esteem grows when you challenge negative thoughts and replace them with positive affirmations.",
            "Remember that your value isn't defined by external achievements. You're worthy just as you are."
        ])
    elif "loneliness" in user_message:
        return random.choice([
            "Loneliness is tough. Reach out to someone you trust, even for a brief conversation—it can make a big difference.",
            "Joining a club or group activity might help combat feelings of loneliness. You're not alone in feeling this way.",
            "Loneliness can feel overwhelming, but spending time doing things you enjoy can help shift your focus."
        ])
    elif "overwhelm" in user_message:
        return random.choice([
            "Feeling overwhelmed? Break tasks into smaller steps and tackle one thing at a time.",
            "It’s okay to feel overwhelmed. Give yourself permission to take a break and reset.",
            "When everything feels like too much, try to focus on what’s within your control and let go of the rest."
        ])
    elif "disappointment" in user_message:
        return random.choice([
            "Disappointment is a part of life, but it doesn’t define you. Reflect on what went wrong and move forward.",
            "It’s okay to feel disappointed. Take time to process your emotions before deciding your next steps.",
            "Disappointment is temporary. Use it as motivation to try again and push through challenges."
        ])
    elif "focus" in user_message:
        return random.choice([
            "If you're struggling with focus, try the Pomodoro technique: work for 25 minutes, then take a short break.",
            "Eliminate distractions, like your phone or background noise, to help improve focus.",
            "Sometimes switching tasks or environments can improve focus and keep you engaged."
        ])
    elif "self-doubt" in user_message:
        return random.choice([
            "Self-doubt happens to everyone. Focus on your past successes to remind yourself of what you're capable of.",
            "When in doubt, remember that learning from failures is just as valuable as achieving success.",
            "Challenge your self-doubt by recognizing your strengths and all the progress you've made so far."
        ])
    elif "peer pressure" in user_message:
        return random.choice([
            "Peer pressure can be tough. Stay true to your values and trust your instincts, even if it’s difficult.",
            "You don’t have to say 'yes' to fit in. Real friends respect your boundaries and choices.",
            "If you're feeling pressured, practice saying 'no' in a firm but kind way. Your well-being comes first."
        ])
    elif "confidence in social situations" in user_message:
        return random.choice([
            "Feeling nervous in social situations is normal. Focus on listening and engaging with others one-on-one.",
            "Confidence in social settings grows with practice. Start small and gradually push your comfort zone.",
            "Don’t worry too much about what others think. Most people are focused on themselves, not judging you."
        ])
    elif "grief" in user_message:
        return random.choice([
            "Grief is a personal journey. Give yourself time and space to feel and process your emotions.",
            "Talking to someone you trust about your grief can help lighten the emotional burden.",
            "Grieving is a natural part of life. Remember that healing takes time, and it's okay to seek support."
        ])
    elif "isolation" in user_message:
        return random.choice([
            "If you’re feeling isolated, try reaching out to someone or participating in a group activity you enjoy.",
            "Isolation can be challenging. Finding online communities or forums can help you feel more connected.",
            "Combat isolation by creating a daily routine that includes virtual or physical social interactions."
        ])
    elif "lack of motivation" in user_message:
        return random.choice([
            "If you're lacking motivation, try setting small goals that are easy to achieve to build momentum.",
            "Sometimes, a lack of motivation means you need to rest. Give yourself permission to recharge.",
            "When motivation is low, focus on your 'why'—what is your long-term goal and why does it matter?"
        ])
    elif "feeling stuck" in user_message:
        return random.choice([
            "Feeling stuck is a sign it might be time for a new approach. Try looking at your challenge from a different angle.",
            "If you’re feeling stuck, taking a break and returning with fresh eyes can help you gain clarity.",
            "Stuck? Write down your thoughts, ideas, or feelings to help organize and make sense of them."
        ])
    elif "friendship issues" in user_message:
        return random.choice([
            "Friendship issues can be painful. It helps to communicate openly and honestly with the person involved.",
            "If you’re having friendship issues, give yourself time to reflect on your feelings before addressing the problem.",
            "Not all friendships last forever, and that’s okay. Focus on the relationships that make you feel valued."
        ])
    elif "exam anxiety" in user_message:
        return random.choice([
            "Exam anxiety is common, but preparation can help. Create a study plan and take breaks to reduce stress.",
            "Before exams, try visualization techniques to imagine yourself staying calm and performing well.",
            "If anxiety is building up before an exam, practice deep breathing or meditation to stay grounded."
        ])
    elif "body image" in user_message:
        return random.choice([
            "Body image can be difficult to navigate, but remember that your worth isn’t tied to appearance.",
            "Focus on what your body can do, rather than how it looks. Celebrate your unique strengths and abilities.",
            "If body image concerns are overwhelming, talking to a counselor or trusted friend can provide perspective."
        ])
    elif "failure" in user_message:
        return random.choice([
            "Failure is a stepping stone to success. Every failure teaches you something valuable.",
            "Don’t fear failure—embrace it as a learning opportunity that brings you one step closer to success.",
            "Failure isn’t final. What matters most is how you bounce back and apply what you've learned."
        ])
    elif "perfectionism" in user_message:
        return random.choice([
            "Perfectionism can create stress. It’s okay to make mistakes as long as you're learning and growing.",
            "Perfectionism can hold you back. Focus on doing your best, not on being flawless.",
            "It’s important to remember that no one is perfect. Be kind to yourself and celebrate progress, not perfection."
        ])
    elif "homesickness" in user_message:
        return random.choice([
            "Homesickness is natural when you're in a new environment. Try staying connected with loved ones regularly.",
            "Focusing on creating a comfortable space or new routines can help ease homesickness over time.",
            "If you’re homesick, remind yourself that adjusting to a new place takes time. Explore your surroundings at your own pace."
        ])
    elif "life balance" in user_message:
        return random.choice([
            "Life balance is key to avoiding burnout. Make time for activities that refresh and recharge you.",
            "If life feels out of balance, try setting boundaries to protect your personal time and well-being.",
            "Maintaining balance is a constant process. Adjust your priorities as needed to stay centered."
        ])
    elif "feeling undervalued" in user_message:
        return random.choice([
            "Feeling undervalued can be disheartening, but remember that your worth isn’t determined by others’ opinions.",
            "If you feel undervalued, it may help to communicate your feelings with those around you or seek validation from trusted sources.",
            "Know that your efforts are valuable even if they aren’t always recognized. Keep focusing on your personal growth."
        ])
    elif "resilience" in user_message:
        return random.choice([
            "Resilience is built through challenges. Every setback is an opportunity to grow stronger.",
            "Remember that resilience isn’t about avoiding hardships, but learning how to adapt and overcome them.",
            "Resilience takes time. Focus on small victories and be patient with yourself as you navigate difficulties."
        ])





    # Add more patterns for different topics as needed
    return "I'm sorry, I don't have a specific answer for that, but it's always good to talk about how you're feeling."
