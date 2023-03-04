import { answer } from '../src/index.js';

describe('index', () => {
	it('should give the answer', () => {
		expect(answer()).toEqual(42);
	});
});
