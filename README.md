# dozen_restful_booker

Contemporary exploratory testing for restful booker

Testing of:

* deployed: <https://automationintesting.online/>
* local build: <https://github.com/mwinteringham/restful-booker-platform>

**S** - **F** - *D* - **P** - **O** - *T*

## Domain

* booking breakfast and bed accommodation

## Features

* contact details of location
* self booking
* contact form
* hide and reveal
* an unresponsive map
* admin functions

## Structure

* multiple views

## Notes on Bugs

* calendar, we can book onli on 1 page
* calendar, we can't cancel booking by clicking on the blue row
* not intuitive
* impossible to choose by clicking on the squares, only on data
* error meaasges are not clear, sometimes it is wrong, inconsistent
* text aligning issue in Cookies and Pprivasy Police
* Newingtonfordburyshire/Newfordburyshire
* The map is not responsive
* We can’t search for street
* The subject icon is envelope, that’s confusing
* The phone number range is weird - whose number is 11 - 22 characters?
* The message range is weird 20 - 2000 prevents shorter messages
* It shows 2 error messages about empty message-field and subject - same field two error messages
* The response is not too pretty
  * The The fonts are not in line, size etc
  * The lining up is bad, Mabel H! aligning issues in forms
  * The message is blunt - try more polite
* error message order varies with same input
* The email doesn’t require the “.”
* The language in page is not too sophisticated
* The Error messages are not consistent with style capitalising
* Error messages should be placed better
* How do I book this =)
  * Calendar not responsive, reactive
  * Error messages are baaaaad!!!
  * Must not be null? We have something everywhere
  * Everything we said about the error messages also apply on booking as even worse
  * Availability not available
* The language, is it some lorem ipsum or?
* The wheelchair icon, what is that?
* we cannot choose the date in Calendar, it is not clickable
* The error message is not clear in Book this room: “Must not be null”
* The map is not working: no zoom, no clicks
* It is also not a proper image as we cannot copy it as other pictures
* In “Thanks for getting in touch ”, the message is split into three lines, while it would be way better to have one clear sentence.
* Different languages on the same webpage
* Links at the footer open webpage in the middle: Cookie-Policy - Privacy-Policy
* Short names are not welcome: Na Li in booking
* We can input everything to Phone Number
* Name and surname can be meaningful
* SQL injection, security issues?
* When I update the webpage, there are some error messages for some milliseconds

## APIs

* Auth        <http://localhost:3004/auth/swagger-ui/index.html>
* Branding    <http://localhost:3002/branding/swagger-ui/index.html>
* Room        <http://localhost:3001/room/swagger-ui/index.html>
* Assets (*)  <http://localhost:3003/assets/swagger-ui/index.html>
* Booking     <http://localhost:3000/booking/swagger-ui/index.html>
* Report      <http://localhost:3005/report/swagger-ui/index.html>
* Message     <http://localhost:3006/message/swagger-ui/index.html>
* Health      <http://localhost:3003/actuator/health>
* Logs        <http://localhost:3003/actuator/logfile>
