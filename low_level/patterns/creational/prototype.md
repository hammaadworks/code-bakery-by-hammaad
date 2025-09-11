1. Analogy
- master blueprint for designing houses.
- biological STEM CELLS
  - it is a master object that can be cloned and modified to specialized organ cells
- game character enemy bulk spawning
  - not every enemy is spawning in mass as that will create runtime object creation bottleneck from class.
  - instead game engine spawns new enemy from enemy prototype with slight change in color and weapon
- cheaper to copy objects than to instantiate one from scratch.
- object becomes a template for another object.

2. Definition
- Prototype is a creational design pattern that
- creates new objects by cloning existing object (prototype)
- instead of instatiating from scratch
- useful when 
  - object creation is expensive (db state, deep object graph, network calls)
  - need similar objects in bulk with slight change
+ Cloning over instantiation -> avoids expensive constructor logic
+ Creation cost reduction
+ structural consistency
+ ploymorphic duplication 

Diff:
factories are like creating a dish from ingredients
prototype is cloning a master dish and adding garnishes