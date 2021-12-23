// format: [length, on_or_off]
var SHORT = [1, true];
var LONG = [3, true];
var GAP = [1, false];
var CHAR_GAP = [3, false];
var WORD_GAP = [7, false];

var INSTRS = {
	'.': SHORT,
	'-': LONG,
	' ': CHAR_GAP,
	'/': WORD_GAP,
};

var TICK_MS = 150;

var CHARS = {
	'0': '-----',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',

	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',

	'+': '.-.-.',
	'-': '-....-',
	'_': '..--.-',
	'"': '.-..-.',
	' ': '/',
};

function str2morse(s) {
	var r = [];

	s = s.toUpperCase();
	for (var i = 0; i < s.length; i++) {
		r.push(CHARS[s[i]]);
	}
	return r.join(' ');
}

function morse2instructions(m) {
	var r = [];
	var p = false;

	m = m.replace(' / ','/');
	for (var i = 0; i < m.length; i++) {
		if (m[i] == '-' || m[i] == '.') {
			if (p) {
				r.push(GAP);
			}
			p = true;
		} else {
			p = false;
		}
		r.push(INSTRS[m[i]]);
	}
	return r;
}

var TIMER = 0;

function play_instructions(ins, elem) {
	ins = ins.slice();

	var f = function() {
		if (!ins.length) {
			elem.style.color = '#F0F0C9';
			TIMER = 0;
			return;
		}

		var c = ins.shift();
		var bg = 0;
		if (c[1]) {
			bg = '#F05D5E';
		} else {
			bg = '#F0F0C9';
		}
		elem.style.color = bg;
		TIMER = window.setTimeout(f, c[0] * TICK_MS);
	};

	f();
}

function stop() {
	if (TIMER) {
		window.clearTimeout(TIMER);
	}
	TIMER = 0;
	document.getElementById('bemVindos').style.color = '#F0F0C9';
}

function go(morse) {
	stop();

	TICK_MS = 150;
	play_instructions(morse2instructions(morse), document.getElementById('bemVindos'));
}
