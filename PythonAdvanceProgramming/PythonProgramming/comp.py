#comphresion-create lists using a single line of code instead of loop
#syantax
#[expression for item in iterable if condition]
#square of a number

sqs=[x**2 for x in range (1,6)]
print(sqs)

#with the condition
evennumbers = [x for x in range(10) if x%2 == 0]
print(evennumbers)

#dict comphresion - increase by 10%
salary = {"A":50000,"B": 60000,"C":70000}
updated_sal={k:v+0.1*v for k, v in salary.items()}
print(updated_sal)


#filtering of dict
employess={
    "Harsha":"ACTIVE",
           "Amit":"INACTIVE",
           "Ravi":"ACTIVE"
}
active_employees = {k:v for k, v in employess.items() if v == "ACTIVE" }
print(active_employees)

#set comphresion
sqs = {x**2 for x in range (1,6)}
print(sqs)

#with the condition
evennumbers= {x for x in range(10) if x%2==0}
print(evennumbers)

