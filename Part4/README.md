# Part 4

## Make a robot learn.

This part of the camp is somewhat special, and perhaps the coolest of them all. Well, it's not just because there isn't any task and evaluation, rather it is because it's about the **brains**, of the robots that we build. Up until now, we had seen various concepts concerning robot anatomy, design structure, and control but hardly anything about planning or decision making related techniques. This is perhaps the most crucial element of the robot. The **robustness, versatility, and generalizing capability** of a control algorithm greatly matter in the real-world deployment of such robots.

<p align="center">
   <img  width="500" height="350" src="https://i.imgur.com/5C7upTs.jpg">
</p>

This is perhaps the general opinion and concern about robots being intelligent and evolving but in reality...

<p align="center">
   <img  width="500" height="500" src="https://cdn-images-1.medium.com/freeze/max/1000/1*x7P7gqjo8k2_bj2rTQWAfg.jpeg?q=20">
</p>

Thus, it all funnels down to simple math, and nothing fancy up until now. All the intelligent machines that have been up until now could be closely compared with a **smart washing machine** and not the much fantasized **AGI** with super-human intelligence and capabilities. We are currently in the age of **Narrow AI**, where the goal is to learn and excel or reach super-human abilities in that particular aspect. Hence, like any other field, the advent of AI has interesting directions in robotics as well. Without getting into much to the depths of AI and its definitions, it's quite reasonable to limit ourselves that we will be dealing with its subset **Machine Learning**.

<p align="center">
   <img  width="500" height="500" src="https://miro.medium.com/max/631/1*TiORvHgrJPme_lEiX3olVA.png">
</p>

In a nutshell, we are trying to make a program make sense out of tons of data fed into it without having to do it explicitly. This kind of data-driven approach can be greatly exploited in robotics, as at times it becomes highly impossible to predict all possible outcomes that our robot could face. So, constraining ourselves to only _Neural Network_ related approaches, an Artificial Neural Network (ANN) is essentially nothing but a function approximator that could map a set of input labels to output labels. I feel sorry for not doing much justice to the definition and oversimplifying things but our prime motive is to get to the application of such ANNs in robotics. For more insights into ANN's...

<div align="center">
  
  [Neural Network series,by 3blue1brown](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)

</div>

On that note, we now have a mathematical system that could learn given the data. So how do we give the data?
Well based on the nature of data, we can classify our approaches broadly into 3.

1. Supervised Learning,_where the dataset is static and labeled in nature_
2. Unsupervised Learning,_where the data set is static and unlabelled_
3. Semi-Supervised Learning,_were the data is dynamic and may or may not be labeled_

Most of you might be quite familiar with the first two types listed above but concerning robotics, we are mostly interested in the third type. Take a minute and think why that should be the case?

_You are right, If you are answer was to make our life miserable and hard..:-)_

On a more serious note, the data that we are talking about robots are from its sensors, be it image feed from a camera, orientation data from an IMU, distance from an ultrasonic sensor, all these have a similarity that makes semi-supervised learning the only possibility and that is,
<div align = "center">
   
Uncertainty in responding to a given senor data,_- meaning our robot cannot always act the same way if it sees the same set of sensor readings. Thus, making its decision-making capabilities rely more on the experience it gained as well and not just the raw input. This makes the nature of our dataset dynamic_

</div>

## Robot learning:

So basically we want **to learn efficient control over a given amount of data for our robot**. Thought the simpler it might sound it has implications of great magnitude that need to be explained and personally experienced to master. Thus, the videos below give a general overview of such methodologies, and getting into a greater depth will require the prolonging of the camp. Thus, we feel that you will be greatly benefited and understand the significance of this topic if we bring it to you as **a series of workshops upon reaching the campus**. For now, we would like you to build on the fundamentals of ML, for the ones who are interested.

1. Open AI's work in Robotics.
   1. [Learning dexterity](https://openai.com/blog/learning-dexterity/)
   2. [Learn to Imitate](https://openai.com/blog/robots-that-learn/)
   
2. [Walk the way you want](https://www.youtube.com/watch?v=iNL5-0_T1D0)
3. [Self,taught goofines-by DeepMind](https://www.youtube.com/watch?v=hx_bgoTF7bs)
4. [Machine Learning in control](https://www.youtube.com/watch?v=3yU2k8R9JeU&list=PLMrJAkhIeNNQkv98vuPjO2X2qJO_UPeWR&index=28)
5. Genetic Algorithm, nature's way of doing it
   1. [Flap till you are the Fittest](https://www.youtube.com/watch?v=aeWmdojEJf0)
   2. [MarI/O](https://www.youtube.com/watch?v=qv6UVOQ0F44)
6. Walk your way to the world
   1. [Sim to real](https://www.youtube.com/watch?v=lUZUr7jxoqM&feature=emb_rel_pause)
   2. [Traing in hardware](https://www.youtube.com/watch?v=FmMPHL3TcrE&feature=youtu.be)
  
If its all greek to you and you still want to pursue this and get to to nuts and bolts of the driving concepts all we can say you now is,


<p align="center">
   <img  width="300" height="150" src="https://thumbs.gfycat.com/EnchantingDecisiveCurlew-max-1mb.gif">
</p>

We will be greatly glad to have you in the workshops that we will be conducted and onboard working on projects with such concepts.We will be dealing from the **very basics to the state of the art concepts of robot learning**. In today's scenario, the required fundamentals for mastering Ml is just a Google search away.

<div align="center">

_Google your way towards learning how to learn_

</div>
