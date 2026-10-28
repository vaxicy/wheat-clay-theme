// Wheat Clay Theme — oat paper, khaki and stone
import { readFile } from 'node:fs/promises';

const CLAY_PALETTE = {
  paper: '#EBE2CC',
  oat: '#DED6C1',
  khaki: '#CFC6B1',
  stone: '#B7B09E',
};

export class ClayField {
  constructor(name = 'Dry border') {
    this.name = name;
    this.palette = CLAY_PALETTE;
  }

  /** Blend two clays into a softer earth tone. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readPlan(file) {
    const content = await readFile(file, 'utf8');
    const rows = content.split('\n').filter(Boolean);
    return {
      name: this.name,
      tones: Object.keys(this.palette).length,
      rows: rows.length,
      content,
    };
  }
}

const field = new ClayField();
const soil = field.blend(CLAY_PALETTE.khaki, CLAY_PALETTE.stone);

console.log(`soil tone: ${soil}`);
