import os
import json
import jsonlines

def jsonl_to_dict(sample_file_name, results, json_filename):
    counter = 0
    with jsonlines.open(os.path.join(main_path, sample_file_name)) as reader:
        for obj in reader:
            results[counter] = obj
            counter += 1

    with open(os.path.join(main_path, json_filename), 'w') as fp:
        json.dump(results, fp)
    return results

def json_to_words(results):
    words_per_sentence = {}
    for i in range(0, len(results)-1):
        result = results[i]
        sentence = result['text']
        words_in_sentence = {}  
        counter = 0
        for annotation in result['annotations']:
            words_i = {}
            words_i['user'] = annotation['user']
            words_i['fraud_tagged'] = sentence[annotation['start_offset']:annotation['end_offset']]

            words_in_sentence[counter] = words_i
            counter += 1

        words_per_sentence[result['id']] = words_in_sentence
    return words_per_sentence

if __name__ == "__main__":
    main_path = os.path.abspath(os.path.dirname(__file__))
    results = {}

    # TODO include option to provide file name as argument
    results = jsonl_to_dict('file_results.jsonl', results, 'results_processed.json')

    words_per_sentence = json_to_words(results)
    print(words_per_sentence)