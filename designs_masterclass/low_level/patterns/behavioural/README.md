# 🎯 Behavioral Design Patterns – LLD Interview Notes

## 🧠 What are Behavioral Design Patterns?

Behavioral Design Patterns define
- **communication rules between objects** i.e. object interactions.
- **responsibility delegation** i.e. distribution of responsibilities amongst objects.
- **runtime behavioral flexibility**
- **object collaborations**.

They promote:
- Strong adherence to **SOLID** principles like **SRP**, **OCP**, and **DIP**.
- **Decoupled object interactions**.
- Dynamic behavior changes at runtime.

> Playbooks for how objects talk, react, and cooperate under various scenarios in a system.
> - define object interactions and responsibility delegation amongst themselves.
> - enable dynamic runtime behavioural flexibility.
> - promote SOLID principles (SRP, OCP, DIP).

---

### 1. [🧬 Template Method](template.ipynb)

> **Consistent flow, customizable steps**

- **Intent**: Define the *algorithm structure* in the *base class*; let *subclasses override* specific steps.
- **Keywords**: 
    - **Open/Closed Principle**
    - **Inversion of Control**
    - **Compile-time Polymorphism**
    - *Abstract Base Class*
    - *Template Hook Method*
    - *Concrete Subclasses*
- **Analogy**:
    - Following a standard *chai-making process*, but each household customizes spices or sugar.
    - *School morning assembly* routine: steps are fixed, but announcements differ.
- **Use Case**:
    - *Data processors*
    - *Report generators*
    - *Onboarding flows*
    - *ETL pipelines*
- **Extra**: 
    - Avoids **code duplication**; promotes **reuse**; enforces **structure**.
    - **Open/Closed Principle**: Enforces *invariant structure* with *controlled extension*.
    - **Dependency Inversion**: High-level modules are *independent of low-level implementations*; they depend only on *abstract hooks*, not on *concrete subclass implementations*.
    - **Hollywood Principle**: *"Don't call us, we'll call you"* — the *base class* calls *subclass-defined methods*.
    - Use **Strategy Pattern** for *runtime polymorphism of algorithm*.

---

### 2. 🔄 State

- **Intent**: Change object behavior based on its internal state, as if it's a different class.
- **Keywords**: Context, State transition, Finite State Machine (FSM).
- **Analogy**:
  - Indian Railway ticket status (`WAITING`, `CONFIRMED`, `CANCELLED`) – different behavior.
  - A fan with speed modes – same button, different outcomes based on state.
- **Use Case**: Order lifecycle, form wizards, media players.
- **Extra**: Replaces large conditional logic; uses composition.

---

### 3. 🧾 Command

- **Intent**: Encapsulate actions into objects to enable queuing, undoing, or logging.
- **Keywords**: Invoker, Receiver, Command Object.
- **Analogy**:
  - Swiggy order: App sends the request, delivery partner executes it.
  - Remote control: button press triggers a command to the TV.
- **Use Case**: Undo/Redo, Menu actions, Scheduling jobs.
- **Extra**: Decouples sender/receiver; enables logging and macros.

---

### 4. 🧠 Strategy

- **Intent**: Define a set of interchangeable algorithms, usable at runtime.
- **Keywords**: Context, Algorithm encapsulation, Composition.
- **Analogy**:
  - Choosing Ola auto, mini, or prime during booking.
  - Selecting UPI, Netbanking, or COD while shopping online.
- **Use Case**: Sorting strategies, pricing engines, payment methods.
- **Extra**: Avoids conditionals; allows runtime behavior injection.

---

### 5. 📢 Observer

- **Intent**: One-to-many dependency; notify all observers on subject change.
- **Keywords**: Subject, Subscriber, Event Push.
- **Analogy**:
  - YouTube channel: subscribers get notified when new video is uploaded.
  - College notice board: students check updates when new notice is pinned.
- **Use Case**: UI updates, notifications, stock price changes.
- **Extra**: Enables reactive systems, loose coupling.

---

### 6. 🧳 Visitor

- **Intent**: Add new operations to objects without changing their structure.
- **Keywords**: Visitor, Accept, Double Dispatch.
- **Analogy**:
  - CA visiting multiple departments during auditing — applying logic based on department.
  - Income Tax officer visiting different types of businesses with unique checks.
- **Use Case**: AST parsing, financial reporting tools.
- **Extra**: Adds behavior without modifying classes, useful for structure-heavy systems.

---

### 7. 🔁 Iterator

- **Intent**: Provide sequential access to elements without exposing internal representation.
- **Keywords**: Cursor, HasNext(), Iterable abstraction.
- **Analogy**:
  - Scrolling through WhatsApp messages one by one.
  - Browsing books in a library rack without knowing arrangement system.
- **Use Case**: Collections, custom data traversal.
- **Extra**: Promotes encapsulation; supports lazy traversal and safe iteration.

---

### 8. 🧭 Mediator

- **Intent**: Centralize communication logic between objects to reduce coupling.
- **Keywords**: Mediator, Colleague, Message router.
- **Analogy**:
  - School teacher resolving student disputes instead of students arguing.
  - WhatsApp group admin coordinating all group decisions.
- **Use Case**: UI components, messaging systems.
- **Extra**: Reduces object entanglement; single point of communication logic.

---

### 9. 🧠 Memento

- **Intent**: Save and restore an object’s state without breaking encapsulation.
- **Keywords**: Originator, Caretaker, Snapshot.
- **Analogy**:
  - Hitting “Save Draft” in Gmail and later resuming.
  - Undoing changes in MS Word using Ctrl+Z.
- **Use Case**: Undo/redo systems, checkpoints in games.
- **Extra**: Enables rollback features; keeps state isolated.

---

### 10. 🧮 Interpreter

- **Intent**: Define a grammar and provide an interpreter to evaluate expressions.
- **Keywords**: Expression tree, Terminal, Recursive parse.
- **Analogy**:
  - Calculator solving `2 + 3 * 4` by following BODMAS.
  - Interpreting simple Hindi-to-English commands like “kaam chalu karo” → “start work”.
- **Use Case**: Regex engines, DSLs, config evaluators.
- **Extra**: Ideal for structured text processing; uses recursion and composition.

---

### 11. 🔗 Chain of Responsibility

- **Intent**: Let multiple handlers process a request sequentially until one handles it.
- **Keywords**: Handler, Request forward, Chain setup.
- **Analogy**:
  - Escalating an issue in a company: Intern → Team Lead → Manager.
  - Customer care call routing: Bot → Agent → Supervisor.
- **Use Case**: Logging, request pipelines, validation chains.
- **Extra**: Decouples request sender and handlers; supports dynamic chains.

---

### 12. 🚫 Null Object

- **Intent**: Provide a no-op default object to avoid null checks.
- **Keywords**: Safe default, Polymorphic stub.
- **Analogy**:
  - Unassigned class monitor who does nothing but avoids errors.
  - Placeholder profile photo when user hasn't uploaded one.
- **Use Case**: Logging, default configs, optional services.
- **Extra**: Prevents null pointer crashes; encourages safe fallback behavior.

---

## 🧾 Quick Recall Table

| Pattern            | Analogies (Indian/Relatable)                           | Key Use Case                       |
|--------------------|--------------------------------------------------------|------------------------------------|
| Template           | Chai recipe, School assembly                           | File processing, workflows         |
| State              | Railway ticket status, Fan speed modes                 | Media players, lifecycle tracking  |
| Command            | Swiggy order, Remote control                           | Undo, Task scheduling              |
| Strategy           | Ola ride type, Payment mode                            | Pricing, search filters            |
| Observer           | YouTube channel, Notice board                          | Notifications, Event systems       |
| Visitor            | CA audit, Tax inspector                                | AST traversal, reporting engines   |
| Iterator           | WhatsApp scroll, Library browsing                      | Custom collections                 |
| Mediator           | Teacher mediator, WhatsApp admin                       | UI logic, Chatroom manager         |
| Memento            | Gmail drafts, Word undo                                | Undo-redo, game checkpoints        |
| Interpreter        | Calculator BODMAS, Hindi-English commands              | Regex, DSL                         |
| Chain of Resp.     | Issue escalation, Customer care routing                | Logging, Auth pipeline             |
| Null Object        | Unassigned monitor, Placeholder profile                | Logging, Default services          |

---
