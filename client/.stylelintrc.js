module.exports = {
    extends: 'stylelint-config-recommended',
    rules: {
        'indentation': 4,
        'at-rule-no-unknown': [
            true,
            {
                'ignoreAtRules': [
                    'define-mixin',
                    'mixin',
                    'if',
                    'else'
                ]
            }
        ],
        'no-descending-specificity': [
            true,
            {
                'severity': 'warning'
            }
        ]
    }
}
