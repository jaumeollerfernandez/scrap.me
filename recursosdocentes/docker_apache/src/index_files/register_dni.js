define(['jquery'],function($){var allowedFistLetter=['A','B','C','D','F','G','H','J','N','P','Q','R','S','U','V','W'];var inLetters=['P','Q','S','W'];var inNumbers=['A','B','E','H'];var errorMiss="DNI: 12345678Z";function checkFirstLetter(nif){var firstLetter=nif[0];firstLetter=firstLetter.toUpperCase();if(allowedFistLetter.includes(firstLetter)){return false;}
return true;}
function checkAreNumbers(nif){var numbers=nif.substring(1,8);if(isNaN(numbers)){return true;}
return false;}
function sumPairs(nif){var sum=0;for(var i=2,len=6;i<=len;i=i+2){sum+=parseInt(nif[i]);}
return sum;}
function sumOdds(nif){var sum=0;var num=0;var digit=0;for(var i=1,len=7;i<=len;i=i+2){num=parseInt(nif[i])*2;while(num>=10){digit=num%10;sum+=digit;num=(num-digit)/10;}
sum+=num;}
return sum;}
function shouldBeLetter(nif){var firstLetter=nif[0];firstLetter=firstLetter.toUpperCase();if(inLetters.includes(firstLetter)){return true;}
return false;}
function shouldBeNumber(nif){var firstLetter=nif[0];firstLetter=firstLetter.toUpperCase();if(inNumbers.includes(firstLetter)){return true;}
return false;}
function getLetter(E){var letters=['J','A','B','C','D','E','F','G','H','I'];return letters[E];}
function checkLastLetter(nif){var sumaA=sumPairs(nif);var sumaB=sumOdds(nif);var C=sumaA+sumaB;var E=C%10;if(E!=0){E=10-E;}
if(shouldBeLetter(nif)){var letter=getLetter(E);if(letter==nif.slice(-1)){return false;}
return true;}else if(shouldBeNumber(nif)){var last=nif.slice(-1);if(isNaN(last)){return true;}else{last=parseInt(last);}
if(E==last){return false;}
return true;}else{var last=nif.slice(-1);var letter=getLetter(E);if(letter==last){return false;}
if(isNaN(last)){return true;}else{last=parseInt(last);}
if(E==last){return false;}
return true;}
return false;}
function checkNif(nif){if(nif.length!=9){return false;}
if(checkFirstLetter(nif)){return false;}
if(checkAreNumbers(nif)){return false;}
if(checkLastLetter(nif)){return false;}
return true;}
function checkAreNumbersDni(dni){var numbers=dni.substring(0,8);if(isNaN(numbers)){return true;}
return false;}
function checkDniLastLetter(dni){var letters=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E'];var numbers=parseInt(dni.substring(0,8));var result=numbers%23;if(letters[result]==(dni.slice(-1).toUpperCase())){return false;}
return true;}
function checkDni(dni){if(dni.length!=9){return false;}
if(checkAreNumbersDni(dni)){return false;}
if(checkDniLastLetter(dni)){return false;}
return true;}
function checkFirstLetterNie(nie){var letter=nie.charAt(0).toUpperCase();var letters=['X','Y','Z'];if(letters.indexOf(letter)==-1){return true;}else{return false;}}
function checkNieNumbers(nie){var letters=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E'];var n_letters=['X','Y','Z'];var letter=nie.charAt(0).toUpperCase();var index=n_letters.indexOf(letter);var new_nie=index+nie.substring(1,8);var numbers=parseInt(new_nie);var result=numbers%23;if(letters[result]==(nie.slice(-1).toUpperCase())){return false;}
return true;}
function checkNie(nie){if(nie.length!=9){return false;}
if(checkFirstLetterNie(nie)){return false;}
if(checkNieNumbers(nie)){return false;}
return true;}
$('.form-create-account > .actions > .action.submit').click(function(event){if(!$("body").hasClass("customer-account-create")){return;}
console.log("customer");var value=$("input[name=taxvat]").val();var isValid=false;var clubwala=$("input[name=clubwala]:checked").val();if((clubwala==undefined)||(clubwala==0)){return;}
if(checkDni(value)||checkNie(value)){isValid=true;}
if(!isValid){$("#vat_id_error").removeClass('hidden');event.preventDefault();}else{$("#vat_id_error").addClass('hidden');}});});