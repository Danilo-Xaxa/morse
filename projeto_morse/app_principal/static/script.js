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

var TICK_MS = 150; // não seria 125?

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

function piscar(morse) {
	stop();

	play_instructions(morse2instructions(morse), document.getElementById('bemVindos'));
}
