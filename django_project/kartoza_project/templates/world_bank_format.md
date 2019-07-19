|         |            |
| ------------- |-------------|
|Assignment name: <br/>**{{ project.title }}** | Approx. value of the contract (in current US$): <br>{{ project.approximate_contract_value }} 
|Country: <br> {{ project.country }} |Duration of assignment (months): <br> {{ project.duration_of_assignment }}   
|Name of Client(s): <br> {% for c in clients %} {{ c.title }} <br> {% endfor %} | Total No. of staff-months of the assignment:  {{ project.total_staff_months }}    
|Contact Person, Title/Designation, Tel. No./Address: <br> {{ project.contact_person.name }}, {{ project.contact_person.telephone }} |    
|Start Date (month/year): {{ project.date_start }} <br> End Date (month/year): {{ project.date_end }} | No. of professional staff-months provided by your consulting firm/organization or your sub consultants:  {{ project.total_staff_months_by_kartoza }}          
|Name of associated Consultants, if any: <br> {% for c in consultants %} <br> {{ c.name }} ({{ c.role }}) <br> {% endfor %} | Name of senior professional staff of your consulting firm/organization involved and designation and/or functions performed (e.g. Project Director/Coordinator, Team Leader): <br> {% for c in staff %} {{ c.name }} ({{ c.role }}) <br> {% endfor %}  

**Description of Project:** <br> <div>{% autoescape off %}{{ project.description }}{% endautoescape %}</div>  
**Description of actual services provided by your staff within the assignment:** <br> <div>{% autoescape off %}{{ project.services_provided }}{% endautoescape %}</div>
