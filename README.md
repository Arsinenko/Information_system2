```mermaid
classDiagram
direction BT
class Booking {
   int id_client
   int id_working_space
   datetime start_time
   datetime end_time
   nvarchar(50) status
   money total_cost
   nvarchar(50) payment_method
   int id
}
class Client {
   nvarchar(50) login
   binary(64) password
   nvarchar(50) first_name
   nvarchar(50) middle_name
   nvarchar(50) last_name
   int id
}
class Club {
   nvarchar(50) address
   nvarchar(50) _name
   varchar(8) phone
   nvarchar(50) working_hours
   int seats_count
   int employees
   int id
}
class Employee {
   nvarchar(50) login
   binary(64) password
   nvarchar(50) passport_data
   date hire_date
   int id_user
   int id_role
   money salary
   int id
}
class Equipment {
   nvarchar(50) type
   nvarchar(80) _name
   nvarchar(120) specification
   date purchase_date
   money purchase_price
   int id_club
   int status
   int quantity
   int id
}
class EquipmentMaintenance {
   int equipment_id
   datetime maintenance_date
   nvarchar(max) description
   money cost
   int id
}
class EquipmentStatus {
   nvarchar(50) _name
   int id
}
class Feedback {
   int id_club
   int id_client
   int rating
   nvarchar(max) comment
   datetime feedback_date
   int id
}
class Payment {
   varbinary(256) encrypted_card_number
   varbinary(265) encrypted_CVV
   date link_date
   int client_id
   int id
}
class Role {
   nvarchar(50) _name
   int id
}
class Shift {
   int id_employee
   datetime start_time
   datetime end_time
   int id
}
class UserActionLog {
   int client_id
   nvarchar(50) action
   datetime action_date
   int id
}
class Working_space {
   int id_equipment
   nvarchar(50) status
   int id
}

Booking  -->  Client : id_client:id
Booking  -->  Working_space : id_working_space:id
Club  -->  Employee : employees:id
Employee  -->  Role : id_role:id
Equipment  -->  Club : id_club:id
Equipment  -->  EquipmentStatus : status:id
EquipmentMaintenance  -->  Equipment : equipment_id:id
Feedback  -->  Client : id_client:id
Feedback  -->  Club : id_club:id
Payment  -->  Client : client_id:id
Shift  -->  Employee : id_employee:id
UserActionLog  -->  Client : client_id:id
Working_space  -->  Equipment : id_equipment:id
```
