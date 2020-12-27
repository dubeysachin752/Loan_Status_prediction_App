 
function getGenderValue() {
  var uiGender = document.getElementsByName("uiGender");
  for (var i in uiGender) {
    if (uiGender[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getMarriedValue() {
  var uiMarried = document.getElementsByName("uiMarried");
  for (var i in uiMarried) {
    if (uiMarried[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getDependentsValue() {
  var uiDependents = document.getElementsByName("uiDependents");
  for (var i in uiDependents) {
    if (uiDependents[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getEducationValue() {
  var uiGraduate = document.getElementsByName("uiGraduate");
  for (var i in uiGraduate) {
    if (uiGraduate[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getSelf_EmployedValue() {
  var uiSelfEmployed = document.getElementsByName("uiSelfEmployed");
  for (var i in uiSelfEmployed) {
    if (uiSelfEmployed[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getCredit_HistoryValue() {
  var uiCreditHistory = document.getElementsByName("uiCreditHistory");
  for (var i in uiCreditHistory) {
    if (uiCreditHistory[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}


function onClickedEstimateLoanStatus() {
  console.log("Estimate loan status button clicked");
  var ApplicantIncome = document.getElementById("uiAppInc");
  var CoapplicantIncome = document.getElementById("uiCoAppInc");
  var LoanAmount = document.getElementById("uiLoanAmount");
  var LoanAmountTerm = document.getElementById("uiLoanAmountTerm");
  var Gender = getGenderValue();
  var Married = getMarriedValue();
  var Dependents = getDependentsValue();
  var Education = getEducationValue();
  var SelfEmployed = getSelf_EmployedValue();
  var CreditHistory = getCredit_HistoryValue();
  var PropertyArea = document.getElementById("uiPropertyArea");
  var estLoanStatus = document.getElementById("uiEstimatedLoanStatus");
  var url = "/estimate_loan_status"; 

  $.post(
    url,
    {
      ApplicantIncome: parseFloat(ApplicantIncome.value),
	  CoapplicantIncome: parseFloat(CoapplicantIncome.value),
	  LoanAmount: parseFloat(LoanAmount.value),
	  LoanAmountTerm: parseFloat(LoanAmountTerm.value),
      Gender: Gender,
      Married: Married,
	  Dependents: Dependents,
	  Education: Education,
	  SelfEmployed: SelfEmployed,
	  CreditHistory: CreditHistory,
      PropertyArea: PropertyArea.value,
    },
    function (data, status) {
      console.log(data.estimated_loan_status);
      estLoanStatus.innerHTML =
        data.estimated_loan_status;
      console.log(status);
    }
  );
}