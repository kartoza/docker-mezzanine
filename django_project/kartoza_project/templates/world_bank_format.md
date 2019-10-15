<table>
<tr>
<th>Assignment name: <br/><b>{{ project.title }}</b></th>
<th>Approx. value of the contract (in current US$): <br>{{ project.approximate_contract_value }} </th>
</tr>
<tr>
<td>Country: <br> {{ project.country }}</th>
<td>Duration of assignment (months): <br> {{ project.duration_of_assignment }}</th>
</tr>
<tr>
<td>Name of Client(s): <br> {% for c in clients %} {{ c.title }} <br> {% endfor %}</th>
<td>Total No. of staff-months of the assignment:  {{ project.total_staff_months }}</th>
</tr>
<tr>
<td>Contact Person, Title/Designation, Tel. No./Address: <br> {{ project.contact_person.name }}, {{ project.contact_person.telephone }}</th>
<td>&nbsp;</th>
</tr>
<tr>
<td>Start Date (month/year): {{ project.date_start }} <br> End Date (month/year): {{ project.date_end }}</th>
<td>No. of professional staff-months provided by your consulting firm/organization or your sub consultants:  {{ project.total_staff_months_by_kartoza }}</th>
</tr>
<tr>
<td>Name of associated Consultants, if any: <br> {% for c in consultants %} <br> {{ c.name }} ({{ c.role }}) <br> {% endfor %}</th>
<td>Name of senior professional staff of your consulting firm/organization involved and designation and/or functions performed (e.g. Project Director/Coordinator, Team Leader): <br> {% for c in staff %} {{ c.name }} ({{ c.role }}) <br> {% endfor %}</th>
</tr>
<tr>
<td colspan="2"><b>Description of Project:</b><br/>{% autoescape off %}{{ project.export_html_description }}{% endautoescape %}</th>
</tr>
<tr>
<td colspan="2"><b>Description of actual services provided by your staff within the assignment:</b><br/>{% autoescape off %}{{ project.export_html_services_provided }}{% endautoescape %}</th>

</tr>
</table>
